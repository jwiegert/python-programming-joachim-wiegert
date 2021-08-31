# Linjär regression: huspriser

## 1. Datainhämtning 

Med Sverige som exempel så finns det flera privata och offentliga aktörer att kontakta beträffande statistik kring huspriser. Den Statistiska Centralbyrån[^1] (SCB) delar öppet data om prisindex i kommuner i olika format (ascii/CSV, Excel och i diagram). Svensk mäklarstatisik [^2] får in data från majoriteten av svenska mäklare och även Hemnet [^3] samlar in försäljningsstatistik. Bäst är att kontakta dem direkt och se vilka data de vill dela med sig av.

### Exempel-features: 

- Boarea och trädgårdsarea.

- Antal rum, sovrum, våningar. Finns (inredd) källare?

- Ålder på fastigheten.

- Avstånd till hav/sjö/badplats, serviceställen, centrum, kommunikationer.

## 2. Databearbetning

/att göra operationer på datan, exempelvis filtrera fram specifik data, rensa bort NaNs, ta bort outliers mm
(CSV, JSON)

Som sagt kan data komma i en mängd olika format. Första steget i databearbetningen är således att översätta datan man får in till ett passande format m.h.a. script, eller i värsta fall med Excel-liknande program.

Nästa steg är att visualisera rådatan, det vill säga att plotta huspriser mot alla möjliga features och features mot varandra. Det görs för att se över kvaliteten hos datan; finns det mycket brus eller diverse extremvärden, saknas det data? Brus och extremvärden går att klippa bort, gärna automatiserat, med t.ex. medelvärdesbildning, diskret Fouriertransformering eller Wavelets. Medelvärdesbildningen kan också behöva användas om de olika features innehåller olika mycket data och noggrannheten behöver anpassas.

Efter databearbetningen är det dags att hitta trender i datan inför den linjära regressionen. Hur beror priset på alla olika features? Beror olika features på varandra? Ger vissa features ingen påverkan alls på huspriset? Om features beror på varandra går det att koppla dem så att man minskar antal features och finns det features som inte pvåerkar alls kan man helt enkelt stryka dem helt. Värderna hos vissa features kan också behöva normaliseras om för att underlätta för algoritmerna och för många features kan leda till överanpassningar av data[^4].

## 3. Linjär regression

Linjär regression är att automatiskt anpassa linjära modeller mot uppsättningar features (allmänna referenser här är [^4] och [^]. Grunden är att nyttja den linjära ekvationen *y = kx + m*. Här är *x* en feature formulerad som en vektor och *y* är vårt output, d.v.s., det förutsedda priset. Parametrarna *k* och *m* ger lutning och skärning genom x=0 (vad y är då x=0). Med N features går det istället att skriva

*y = W(0) + W(1) x X(1) + W(2) x X(2) + ... + W(i) x X(i) + ... + W(N) x X(N)*

där *W* är en matris vars element kallas för *Weights* och består av vektorerna *W(i)*. Varje *W(i)* motsvarar linjens lutning *k* för varje feature, förutom *W(0)* som motsvaras av konstanten *m* som gav *y* då *x=0*. I matrisen *X* är varje kolumn *X(i)* en feature.

Den linjära regressionen hittar en uppsättning *W*-element som minimerar skillnaden mellan y och de verkliga priserna. Det går att göra med *cost function*, *J(W)*. Funktionen *J(W)* är en mångdimensionell funktion som går att visualiseras som en yta i ett rum uppspänt av vektorerna *W(i)*. Höga värden hos *J* innebär dålig anpassning till datan och låga värden innebär god anpassning. Ibland finns det flera minima hos *J* men inte hos linjära samband.

För att minimera *J* går det att nyttja *gradient descent*. Den metoden innebär att man tar derivatan av *J* med avseende på alla *W* och följer negativ derivata. Så "vandrar" man nedför "kullarna" av *J* mot ett minimum. Det är viktigt att välja lagom stora "vandringssteg" och ett lämpligt startvärde. För stora vandringssteg gör att man kan missa minimum av *J*, och vandra fram och tillbaka.

## 4. Driftsättning

Det vore praktiskt med en webbaserad tjänst där användaren fyller i värden för de olika features som finns på ett hus och får en uppskattning av priset inom vissa felmarginaler. Modellen bakom bör baseras på uppdaterade data så det behöver finnas ett system som automatiskt hämtar in data myndigheter och mäklare, givetvis med tillstånd. System ska göra en automatisk granskning av datakvaliteten, uppdatera modellen och kompensera för inflation.

Det är vanligt att maskininlärningsprojekt aldrig blir implementerade för användning [^6]. Därför kan det vara nyttigt för en datavetare att lära sig grundläggande driftsättning. Det finns därför en mängd olika verktyg för att underlätta driftsättning[^7]. Vanliga verktyg och aktörer för att träna/uppdatera ML-program, skapa API:er och som säljer serverutrymme är bland annat [Azure ML](https://azure.microsoft.com/), [AutoML](https://www.automl.org/), [IBM Watson ML](https://cloud.ibm.com/apidocs/machine-learning), [TFX](https://www.tensorflow.org/tfx/).

## Teknologier/verktyg

- [Python](https://www.python.org/): praktiskt språk.

- [Numpy](https://numpy.org/): databehandling och matematik.

- [SciPy](https://www.scipy.org/): databehandling och matematik.

- [Pandas](https://pandas.pydata.org/): datanalys.

- [Matplotlib](https://matplotlib.org/): visualisering.

- [Topcat](http://www.star.bris.ac.uk/~mbt/topcat/): visualisering.

- [scikit-learn](https://scikit-learn.org/): visualisering och träna program.

- [TensorFlow](https://www.tensorflow.org/): träna program.

- [Matlab](https://matlab.mathworks.com/): databehandling och visualisering.

## Referenser

[^1]: (2021-08-30) [https://www.scb.se/](https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-byggande-och-bebyggelse/fastighetspriser-och-lagfarter/fastighetspriser-och-lagfarter/)

[^2]: (2021-08-30) [https://www.maklarstatistik.se/](https://www.maklarstatistik.se/)

[^3]: (2021-08-30) [https://www.hemnet.se/](https://www.hemnet.se/bostadsmarknaden)

[^4]: Andrew Ng, Stanford university, [Machine Learning](https://www.coursera.org/learn/machine-learning?).

[^5]: Wieland Wermke, Uppsala universitet, [Statistiska analyser 7- enkel linjär regression](https://media.medfarm.uu.se/play/attachmentfile/video/4787/video.pdf)

[^6]: (2021-08-31) [https://stackoverflow.blog/](https://stackoverflow.blog/2020/10/12/how-to-put-machine-learning-models-into-production/)

[^7]: (2021-08-31) [https://towardsdatascience.com/](https://towardsdatascience.com/10-ways-to-deploy-and-serve-ai-models-to-make-predictions-336527ef00b2)