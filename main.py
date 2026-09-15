from flask import Flask, render_template_string
app = Flask(__name__)
PAGE = """
<center>
<h1>GASY FAUCET</h1>
<h3>Demo Claim</h3>
<input id=w placeholder='0x wallet' style='padding:12px;width:90%'><br><br>
<button onclick='claim()' style='padding:15px;background:#22d3ee;width:90%'>CLAIM</button>
<div id=msg></div>
<div id=tm style='font-size:32px;color:gold;margin:15px'>Vonona!</div>
<script>
let ok=true;
function claim(){
if(!ok)return;
let v=document.getElementById('w').value;
if(v.length<10){alert('Wallet');return}
document.getElementById('msg').innerHTML='Voaray!';
ok=false;let s=300;
let it=setInterval(()=>{
s--;document.getElementById('tm').innerHTML=Math.floor(s/60)+':'+String(s%60).padStart(2,'0');
if(s<=0){clearInterval(it);ok=true;document.getElementById('tm').innerHTML='Vonona!'}
},1000);
}
</script>
</center>
"""
@app.route('/')
def home():
 return render_template_string(PAGE)
if __name__=='__main__':
 app.run(host='0.0.0.0',port=10000)
