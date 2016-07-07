from flask import Flask, request, redirect, url_for
import twilio.twiml

app = Flask(__name__)

@app.route('/')
def step_one():
    """Entry point to respond to incoming requests."""

    resp = twilio.twiml.Response()
    with resp.gather(numDigits=6, action="/post_step_one_logic", method="POST"):
    	resp.say("Hello. This is Contact Guardian. Please enter your pin.")

    return str(resp)

@app.route('/post_step_one_logic', methods=['GET', 'POST'])
def post_step_one_logic():
    """Handle response from step 1"""
    #FIXME Link up to a database

    if request.form['Digits'] == "123456":
    	resp = twilio.twiml.Response()
    	resp.say("Hello {}. You have 3 contacts saved.".format("Dale"))
    	resp.redirect(url="/step_two")
    	return str(resp)
    else:
    	return redirect(url_for('step_one'))

@app.route('/step_two')
def step_two():
    """TODO Step two"""
    return

if __name__ == '__main__':
	app.run()