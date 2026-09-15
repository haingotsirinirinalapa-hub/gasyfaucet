from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html><html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GASY FAUCET</title>

<!-- MONETAG 4 ZONES - GASYFAUCET -->
<script src="https://quge5.com/88/tag.min.js" data-zone="11811636" async data-cfasync="false"></script>
<script src="https://quge5.com/88/tag.min.js" data-zone="11811637" async data-cfasync="false"></script>
<script src="https://quge5.com/88/tag.min.js" data-zone="11811638" async data-cfasync="false"></script>
<script src="https://quge5.com/88/tag.min.js" data-zone="11811639" async data-cfasync="false"></script>

<style>
body{background:#0a0a0a;color:#fff;text-align:center;padding:20px;font-family:sans-serif}
h1{color:#FFD700;margin-bottom:5px}
.box{max-width:360px;margin:20px auto;background:#111;padding:20px;border-radius:12px;border:1px solid #333}
input{width:100%;padding:12px;background:#000;color:#fff;border:1px solid #444;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:13px;margin-top:12px;background:#00D9FF;border:none;border-radius:8px;font-weight:bold;font-size:16px;cursor:pointer}
button:active{transform:scale(0.98)}
#msg{margin-top:15px;color:#00FF88;min-height:20px}
small{color:#888}
</style>
</head>
<body>
<h1>GASY FAUCET</h1>
<small>Claim isaky ny 5 minitra - FaucetPay</small>
<div class="box">
<input type="text" id="wallet" placeholder="Adresse FaucetPay-nao (BTC, LTC, DOGE...)">
<button onclick="claim()">CLAIM NOW</button>
<p id="msg"></p>
</div>
<script>
function claim(){
  var w=document.getElementById('wallet').value;
  var m=document.getElementById('msg');
  if(w.length<10){m.innerText='Ampidiro adresse marina!';return;}
  m.innerText='Miandry 5s... aza miala!';
  setTimeout(function(){m.innerText='✅ 0.00000005 BTC nalefa tamin: '+w;},5000);
}
</script>
</body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
