from flask import Flask, render_template
from settings import key_pair
import boto3
app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')
print "hi"
@app.route("/")
def hello():
    # return "Hello World!"

    ec2 = boto3.client('ec2', region_name=key_pair['region'], aws_access_key_id=key_pair['ACCESS_ID'],
         aws_secret_access_key= key_pair['ACCESS_KEY'])
    ec2 = boto3.client('ec2')
    data = ec2.describe_instances()

    result_dict = {}

    for i in data:
    # print i
        for jj in data['Reservations']:
            # print jj['Instances']
            for k in jj['Instances']:
                if  k['SubnetId']:
                    print "SubnetId is avilable"
                    result_dict['subnet'] = "Go"
                else :
                    print "sunbetid is not available"
                    result_dict['subnet'] = "Not to Go"

                if  k['VpcId']:
                    print "Vpc is avilable"
                    result_dict['vpc'] = "Go"
                else :
                    print "Vpc is not available"
                    result_dict['vpc'] = "Not to Go"

                print k['Monitoring'].get("State")
                if k['Monitoring'].get("State") == "enabled":
                    pass

                print k['SecurityGroups']
                # print k['VpcId'], "^^^^"
        break


    return render_template('output.html', result=result_dict)

if __name__ == "__main__":
    app.run(debug=True)