
#### For å kunne laste opp til GitHub, åpne terminalen og kjør følgene kommandoer:

Dette trenger bare gjøres én gang

* `git config --global user.email "din@mail.com"` (Bruk GitHub mailen)
* `git config --global user.name "ditt navn"`  
(Du kan velge å hete hva du vil, og kan endre det når du vil ved å kjøre kommandoen på nytt)
* Hvis du vil se hva navnet og mailen din er: `git config --list --global`  

<br>

___

<br>

>VSCode har en GUI for alle git kommandoer dere kommer til å trenge, men om dere vil bli bedre kjent med git (og/eller føle dere som hackere) kan dere også bruke git i terminalen (se under)

Bruk gjerne test.py til å prøve dere fram med git

#### Terminalen i vscode:

Hvor du åpner en terminal er ***ikke*** likegyldig. For å kjøre git kommandoer opp mot GitHub må du befinne deg i prosjektet.  
Hvis du har 'IMAA-2022-GRUPPE-FEM' mappa åpen i vscode (**File -> Open Recent** eller **File -> Open Folder...**) kan du gå til:  

**View -> Terminal** eller **Terminal -> New Terminal** eller **Ctrl+Shift+Ø**, for å åpne terminalen _i_ prosjektet

Her kan dere bruke git kommandoer.  

Dere kan også bruke den '_vanlige_' terminalen, men må da passe på at _adressa_ stemmer.  
Dvs. `C:\Users\...\...\...\IMAA-2022-GRUPPE-FEM>`  
                                                   ^^^^^^^^^^^^^^^^^  
Dere kan komme hit ved å skrive `cd "C:\Users\...\...\...\IMAA-2022-GRUPPE-FEM"` i terminalen

#### Noen kommandoer dere kan kjøre i terminalen  

* `git fetch` - Sjekk om det har blitt gjort endringer i GitHub
* `git pull` - Hent alle endringene fra GitHub
* Alternativt kan dere: `git fetch && git pull`
* `git status` - Se hvilke endringer du har lokalt / hvilke filer som er i _staging_
* `git add test.py` - Legg fil til _staging_ | gjør dette med alle filer du vil laste opp
* `git restore --staged test.py` - Fjern fil fra _staging_
    * _Staging_ brukes for å gruppere flere filer bak _én_ commit  

* `git commit -m "..."` - Alle filer i _staging_ blir lagret i git (lokalt ***ikke*** i GitHub)
    * git **krever** at du skriver en log av hva du har endret f.eks. `git commit -m "la til f_dx(x)"`, hold det kort 
    * git ≠ GitHub. Husk du måtte laste ned git, git er et program for versjonskontroll som kjører lokalt på PC'en din.
    * GitHub er en nettside/server som _hoster_ koden og gjør det mulig for andre å hente _commits_ fra _din_ git til _deres_
* `git reset HEAD~1` - Angre forrige commit | prøv å unngå å bruke denne
* `git push` - Last opp alle _commits_ til GitHub
