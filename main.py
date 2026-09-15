from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>GASY FAUCET</title></head>
    <body style="text-align:center; font-family:Arial; padding-top:50px; background:#f0f8ff;">
        <h1 style="color:#007bff;">🚰 GASY FAUCET 🚰</h1>
        <h2 style="color:green;">✓ Site-nao Mandeha!</h2>
        <p>Eto no hanaovanao faucet crypto malagasy</p>
        <button style="padding:15px 30px; background:#007bff; color:white; border:none; border-radius:10px; font-size:18px;">Claim 0.001 MATIC</button>
        <p style="margin-top:30px;">gasyfaucet.onrender.com</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
