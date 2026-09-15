from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<html><head><meta name="monetag" content="c613ba3fbfec476cec0048d1a0ab2807"><meta name="viewport"
content="width=device-width,initial-scale=1">
<style>
body{background:#0a0a0a;color:#fff;
text-align:center;padding:20px}
h1{color:#FFD700}
.box{max-width:360px;margin:auto;
background:#111;padding:20px;
border-radius:12px;border:1px solid #333}
input{width:100%;padding:12px;
background:#000;color:#fff;
border:1px solid #444;border-radius:8px}
button{width:100%;padding:13px;
margin-top:12px;background:#00D9FF;
border:none;border-radius:8px;
font-weight:bold}
</style></head>
<body>
<h1>GASY FAUCET</h1>
<p>0.001 MATIC / 5 min</p>
<div class="box">
<input id="w" placeholder="0x wallet...">
<button onclick="claim()">CLAIM 0.001 MATIC</button>
<p id="t">Vonona!</p>
</div>
<script>
function claim(){
 let x=300;
 let i=setInterval(()=>{
  x--;
  document.getElementById('t').innerHTML=x+'s';
  if(x<=0){
   clearInterval(i);
   document.getElementById('t').innerHTML='Vonona!'
  }
 },1000);
}
</script>
</body></html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)
