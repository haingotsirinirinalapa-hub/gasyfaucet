from flask import Flask, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gasy Faucet</title>
<style>
body{font-family:Arial;text-align:center;padding:20px;background:#f5f5f5}
.box{background:white;padding:20px;border-radius:10px;max-width:400px;margin:auto;box-shadow:0 2px 10px #ccc}
input{width:90%;padding:12px;margin:10px 0;border-radius:8px;border:1px solid #ccc}
button{padding:12px 25px;background:#0a7cff;color:white;border:none;border-radius:8px;font-weight:bold}
.msg{margin-top:15px;font-weight:bold}
</style>
</head>
<body>
<div class="box">
<h2>Gasy Faucet</h2>
<p>Ampidiro ny adresinao</p>
<form method="POST">
<input type="text" name="address" placeholder="Adiresy eto..." required>
<br>
<button type="submit">CLAIM</button>
</form>
<div class="msg">{{ message }}</div>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        address = request.form.get("address", "").strip()
        # ITO NY FANAMBOARANA - tsy henjana be intsony
        if len(address) < 5:
            message = "❌ Ampidiro adresse marina!"
        else:
            message = f"✅ Vita! Nalefa tamin'ny {address} ny valisoa! (Demo)"
    return HTML.replace("{{ message }}", message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
