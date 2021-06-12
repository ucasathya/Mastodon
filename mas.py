from flask import *
from mastodon import Mastodon
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("comment.html")

@app.route("/postmsg",methods = ["POST","GET"])
def postmsg():
    if request.method == "POST":
        try:
            name = request.form["comments"]
            
            mastodon = Mastodon(
    
                access_token = '2QVhZ6IrT2GPTdJ8XJKIpYt_pnrWsJAhekEgg73h0qs',
                api_base_url = 'https://mastodon.social'
            )

            mastodon.status_post(str(name))
            msg = "Message succesfully Posted"
                
        except:
            con.rollback()
            msg = "We can not send Message to Mastodon"
        finally:
            return render_template("success.html",msg = msg)
            


if __name__ == "__main__":
    app.run(debug = True)  

