# shinsou.html（ブラウザ版）から shinsou_suno.html（Suno版）を作る。直すのは shinsou.html だけでよい
import os
D=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(D,'shinsou.html'),encoding='utf8').read()
R=[("const SUNO_ED=false","const SUNO_ED=true"),
   ("<title>THE DEPTHS ECHO ─ 深層の残響</title>","<title>THE DEPTHS ECHO ─ 深層の残響（Suno版）</title>"),
   ("/The-Depths-Echo/main/shinsou.html'","/The-Depths-Echo/main/shinsou_suno.html'")]
for a,b in R:
  assert s.count(a)==1,a;s=s.replace(a,b)
open(os.path.join(D,'shinsou_suno.html'),'w',encoding='utf8').write(s)
print('shinsou_suno.html を作った')
