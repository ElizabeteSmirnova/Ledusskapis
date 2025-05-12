/////////////////////////////////Ēdiena termiņu uzraudzības sistēma//////////////////////////////////////////
Šī programma ir noderīgs rīks ikvienam lietotājam, kas vēlas labāk pārvaldīt pārtikas krājumus savā mājsaimniecībā. Tā palīdz samazināt pārtikas izšķērdēšanu, atgādina par produktiem ar beigušos termiņu un vienkāršo iepirkšanos.
	
/////////////////////////////////Galvenās funkcijas://////////////////////////////////////////////////

Produktu pievienošana: Lietotājs var pievienot jaunus pārtikas produktus, norādot to nosaukumu un derīguma termiņu.
Produktu saraksta apskate: Lietotājs jebkurā laikā var pārskatīt, kādi produkti šobrīd ir ledusskapī.
Produktu izņemšana: Ja produkts ir izmantots vai izņemts, to var dzēst no saraksta.
Brīdinājumu sistēma: Automātiski tiek parādīts paziņojums, ja kādam produktam ir beidzies vai drīz beigsies derīguma termiņš.
Iepirkumu saraksts: Lietotājs var pievienot produktus iepirkumu sarakstam.
Interneta veikalu piekļuve: Iespēja ar vienu klikšķi apmeklēt populārākos Latvijas e-veikalus (Rimi, Maxima, Lidl, Barbora).

//////////////////////////////////Izmantotās Python bibliotēkas un to nozīme/////////////////////////////////////
pandas: Izmanto datu glabāšanai un apstrādei CSV failos. Šī bibliotēka ir būtiska, jo tā nodrošina ērtu veidu, kā lasīt, apvienot, filtrēt un saglabāt datus. CSV faili darbojas kā vienkārša datubāze.

tkinter: Izmanto lietotāja grafiskā interfeisa (GUI) izveidei. Ar tās palīdzību tiek izveidotas pogas, logi un ziņojumi, kas nodrošina intuitīvu lietošanas pieredzi.

datetime: Ļauj strādāt ar datumiem, īpaši derīguma termiņu salīdzināšanai ar šodienas datumu.

os: Tiek izmantota, lai pārbaudītu, vai nepieciešamie CSV faili jau eksistē, un, ja ne – tie tiek izveidoti automātiski.

webbrowser: Nodrošina iespēju atvērt saites uz e-veikaliem tieši no programmas loga.

///////////////////////////////////////////Izmantotās datu struktūras///////////////////////////////////////////
Projektā izmantotas vairākas pielāgotas un strukturētas datu struktūras:

CSV tabulas: Tiek izmantotas kā datu uzglabāšanas forma. "fridge.csv" satur divas kolonnas – “Product” un “ExpiryDate”, savukārt "shopping_list.csv" satur tikai “Product”. Šīs struktūras atvieglo datu glabāšanu un piekļuvi, neizmantojot sarežģītas datubāzes.

pandas DataFrame: Tiek izmantots kā starpformāts datu manipulācijai. Katru reizi, kad tiek pievienots vai dzēsts produkts, tiek manipulēts ar DataFrame objektu.

Saraksts (list): Brīdinājumu veidošanai tiek izmantots Python saraksts, kurā tiek apkopoti produkti ar beigušos vai tuvojošos termiņu.

///////////////////////////////////////////////Programmatūras izmantošana//////////////////////////////////////

Programmas palaišana: Vienkārši palaidiet Python skriptu. Tiks atvērts lietotāja logs.
Produkta pievienošana: Spiediet pogu “Pievieno produktu!” un ievadiet produkta nosaukumu un derīguma termiņu formātā YYYY.MM.DD.
Produktu saraksts: Poga “Rādīt ledusskapja saturu” parāda pašreizējo produktu sarakstu.
Produkta izņemšana: Spiediet “Izņemt produktu” un ievadiet produkta nosaukumu, lai to dzēstu no saraksta.
Derīguma termiņu pārbaude: Poga “Pārbaudīt derīguma termiņus” parāda produktus, kuriem derīguma termiņš ir beidzies vai tuvojas.
Iepirkumu saraksts: Spiediet “Pievienot iepirkumu sarakstam” un ievadiet produkta nosaukumu.
E-veikali: Ar pogu “E-veikali” iespējams izvēlēties vienu no piedāvātajiem tiešsaistes veikaliem un uzreiz atvērt to mājaslapu.
