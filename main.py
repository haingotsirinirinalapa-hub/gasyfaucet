from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gasy Faucet</title>
<style>
body{font-family:Arial;text-align:center;padding:20px;background:#f0f2f5}
.box{background:white;padding:20px;border-radius:15px;max-width:400px;margin:auto;box-shadow:0 4px 10px rgba(0,0,0,0.1)}
input{width:90%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:8px}
button{padding:12px 25px;background:#0a7cff;color:white;border:none;border-radius:8px;font-weight:bold}
.msg{margin-top:15px;font-weight:bold}
</style>
</head>
<body>
<div class="box">
<h2>Gasy Faucet</h2>
<p>Ampidiro ny adresinao</p>
<form method="POST">
<input type="text" name="address" placeholder="Adiresy LTC...">
<br>
<button type="submit">CLAIM 0.1</button>
</form>
<div class="msg">{{ message }}</div>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        address = request.form.get("address", "").strip()
        reward = 0.1  # <--- ETO NO 0,1
        if len(address) < 10:
            message = "❌ Ampidiro adresse marina"
        else:
            message = f"✅ Vita! Nalefa tamin'ny {address[:12]}... ny {reward} LTC! (Demo)"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
