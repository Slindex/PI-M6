# Diccionario de datos

Un importante hospital desea saber las características más importantes que tienen los pacientes de cierto tipo de enfermedad que terminan en hospitalización. Fue definido como:
* **caso** aquel paciente que fue sometido a biopsia prostática y que en un periodo máximo de 30 días posteriores al procedimiento presentó fiebre, infección urinaria o sepsis, lo que termina requiriendo manejo médico ambulatorio u hospitalizado para la resolución de la complicación. 
* **control** al paciente que fue sometido a biopsia prostática y que no presentó complicaciones infecciosas en el período de 30 días posteriores al procedimiento.

Una **biopsia prostática** es una prueba diagnóstica que consiste en extraer una pequeña muestra de tejido prostático mediante un "pinchazo" para luego poder analizarlo y detectar ciertas enfermedades como el cáncer. Suele realizarse a través del recto, introduciendo un transductor ecográfico por el ano y observamos por ecografía la anatomía de la próstata, y luego, con una aguja muy fina, se toman una serie de muestras de tejido de zonas seleccionadas. También es posible realizar la biopsia a través del periné (el espacio que queda entre los testículos y el recto).

Se provee una base de datos con algunos datos referentes a los pacientes y resultados de exámenes diagnósticos, de pacientes hospitalizados y no hospitalizados. En esta recopilación se destacan cuatro grupo de variables Antecedentes del paciente, Morbilidad asociada al paciente y Antecedentes relacionados con la toma de la biopsia y Complicaciones infecciosas.

NOTA: se adviertió que hay algunos problemas de calidad de datos en la información suministrada.

## Antecedentes del paciente

* **EDAD**: Es la edad del paciente. Es un número cuantitativo entero.

## Morbilidad asociada al paciente

* **DIABETES**: Indica si el paciente tiene diabetes o no. Es una variable SI/NO.
* **HOSPITALIZACIÓN ULTIMO MES**: Indica si el paciente fue hospitalizado el mes previo al procedimiento. Es una variable SI/NO.
* **CUP**: Indica el uso de cateter urinario al momento de la biopsia. Es una variable SI/NO.
* **ENF. CRONICA PULMONAR OBSTRUCTIVA**: Indica si el paciente tiene una enfermedad crónica pulmonar obstructiva. Es una variable SI/NO.
* **VOLUMEN PROSTATICO**: Indica si el volumna prostático es mayor a 40 $cm^3$. Es una variable SI/NO.

La próstata está formada por tejido muscular y glandular, cuyo **volumen** normal es de aproximadamente 20 $cm^3$. El crecimiento del tamaño de la próstata es lento y prácticamente inexistente hasta los 30 años, momento en el cual empieza, generalmente a aumentar de tamaño paulatinamente. De forma regulada se establece como el crecimiento medio anual del tamaño de la próstata en torno al 1,6% del volumen prostático cada año hasta la quinta década de la vida en la que aumenta a un ritmo medio de 0,4 g por año hasta el fallecimiento del paciente. Esto significa que la próstata es un órgano en continuo crecimiento y que por tanto, el tamaño normal de la próstata irá aumentará de forma progresiva. Valores superiores a 40 cm3 se consideran un agrandamiento de la próstata más significativo. Cuando el volumen prostático es mayor a 40 $cm^3$, puede causar síntomas y problemas urinarios debido a la compresión de la uretra.

Un **catéter urinario** es un tubo delgado que se pone en la vejiga para drenar la orina.

Una **enfermedad pulmonar obstructiva crónica** (EPOC) es una enfermedad pulmonar común que reduce el flujo de aire y causa problemas.respiratorios.


## Antecedentes relacionados con la toma de la biopsia

* **PSA**: Es la concentración de PSA en sangre. Es una variable del tipo continua.
* **BIOPSIAS PREVIAS**: Indica si el paciente ha tenido biopsias previas. Es una variable SI/NO.
* **ANTIBIOTICO UTILIAZADO EN LA PROFILAXIS**: Indica el tipo de antibiótico utilizado en la biopsia. Es una variable categórica.
    
    Se presentan:
    * *FLUOROQUINOLONA_AMINOGLICOSIDO*
    * *CEFALOSPORINA_AMINOGLUCOCIDO*
    * *OROQUINOLONAS*
    * *OTROS*
* **NUMERO DE MUESTRAS TOMADAS**: Indica el número de muestras tomadas en la biopsia. En un número cuantitativo entero.
* **BIOPSIA**: Es el resultado de la biopsia. Es una variable categórica.
    
    Se presentan como:
    * *NEG*: resultado negativo para cancer prostático.
    * *ADENOCARCINOMA GLEASON 6*: es un cáncer de grado bajo.
    * *ADENOCARCINOMA GLEASON 7*: es un cáncer de grado medio.
    * *ADENOCARCINOMA GLEASON 8*: es un cáncer de grado alto
    * *ADENOCARCINOMA GLEASON 9*: es un cáncer de grado alto
    * *ADENOCARCINOMA GLEASON 10*: es un cáncer de grado alto
    * *PROSTATITIS*: significa inflamación de la próstata.
    * *HIPERPLASIA PROSTATICA*: significa es un agrandamiento no canceroso de la glándula prostática.
    * *CARCINOMA INDIFERENCIADO DE CELULAS CLARAS*: es una tumoración altamente agresiva y los pacientes fallecen en el primer año después del diagnóstico a pesar del ensayo de la radioterapia.

**PSA** significa prueba del antígeno prostático específico. El *antígeno prostático específico* es una proteína que producen tanto las células normales como las células malignas (cancerosas) de la próstata. La prueba del PSA se usa para medir la concentración del PSA en la sangre. Los resultados en general se indican en nanogramos de PSA por mililitro de sangre (ng/ml). 

No hay una concentración específica normal o anormal del PSA en la sangre. Antes, las concentraciones del PSA de 4,0 ng/ml o menos se consideraban normales. Pero algunas personas con concentraciones del PSA inferiores a 4,0 ng/ml tienen cáncer de próstata y muchas personas con concentraciones del PSA más altas, entre 4 ng/ml y 10 ng/ml, no tienen cáncer de próstata. Pero en general cuanto más alta sea la concentración del PSA, más probable es que la persona tenga cáncer de próstata. 

Además, varios factores hacen que la concentración del PSA varíe. Por ejemplo, la concentración del PSA tiende a aumentar con la edad, el tamaño de la próstata, y la inflamación o infección en la próstata. También aumenta la concentración del PSA después de una biopsia de próstata, la eyaculación o el ejercicio vigoroso (como montar en bicicleta) durante los 2 días anteriores a la prueba. Por el contrario, algunos medicamentos, como la finasterida y la dutasterida, que se usan para tratar la hiperplasia prostática benigna , disminuyen la concentración del PSA. 

Es posible que la prueba del PSA dé resultados positivos falsos. Un resultado positivo falso de una prueba indica que la concentración del PSA es elevada, pero no hay cáncer. Un resultado positivo falso de una prueba crea ansiedad y podría llevar a otros procedimientos médicos, como una biopsia de próstata, que podría causar daño. Los posibles efectos secundarios de las biopsias incluyen infecciones graves, dolor y sangrado.
Los resultados positivos falsos en la prueba del PSA son comunes. Solo alrededor del 25 % de las personas que se hacen una biopsia de próstata por una concentración elevada del PSA confirman que tienen cáncer de próstata tras la biopsia.

## Complicaciones infecciosas

* **NUMERO DE DIAS POST BIOPSIA EN QUE SE PRESENTA LA COMPLICACIÓN INFECCIOSA**: indica el tiempo al cual se presenta la complicación infecciosa con un máximo de 30 días. En una variable cuantitativa entera.
* **FIEBRE**: indica si el paciente presenta fiebre. Es una variable SI/NO.
* **ITU**: indica si el paciente presenta infección de tracto urinario. Es una variable SI/NO.
* **TIPO DE CULTIVO**: indica el tipo de cultivo solicitado. Es una variable categorica. 
    
    Entre los Tipos de Cultivos aparecen:
    * *Hemocultivo*: es un examen de laboratorio que permite verificar si hay bacterias u otros organismos en la muestra de sangre del paciente.
    * *Urocultivo*: examen que permite determinar la presencia de una infección urinaria.
    * *Hemocultivo y urocultivo*: cuando se piden ambos estudios.
    * *No*: cuando no se pide ninguno.
* **AGENTE AISLADO**: indica el tipo de agente aislado en el cultivo. Es una variable categórica.
    
    Se indican:
    * *E. Coli*: es una de las bacterias más comúnmente implicadas en el desarrollo de infecciones prostática.
    * *Pseudomonas aeruginosa*: son patógenos oportunistas que con frecuencia causan infecciones intrahospitalarias.
    * *No*: que no se ha aislado agente. 
* **PATRON DE RESISTENCIA**: indica si presenta algún patrón de resistencia a los antibióticos. Es una variable categórica.
    
    Se presentan como:
    * *AMPI*: significa resistencia a la ampicilina.
    * *CIPRO*: significa resistencia a ciprofloxacino.
    * *GENTA*: significa resistencia a gentamicina.
    * *SULFA*: significa resistencia a sulfametoxazol/trimetoprima.
    * *CEFADROXILO*: significa resistencia a cefadroxilo.
    * *CEFUROXIMO*: significa resistencia a cefuroxima.
    * *CEFEPIME*: significa resistencia cefepima.
    * *CEFOTAXIMA*: significa resistencia cefotaxima.
    * *MULTI SENSIBLE*: se refiere un paciente que experimenta resistencia a gran variedad de antibióticos.

* **HOSPITALIZACION**: indica si el paciente fue hospitalizado luego del procedimiento. Es una variable SI/NO.
* **DIAS HOSPITALIZACION MQ**: indica los días de hospitalización médico quirúrgico. En una variable cuantitativa entera.
* **DIAS HOSPITALIZACIÓN UPC**: indica los días de hospitalización en estado crítico. En una variable cuantitativa entera.

Luego de realizar el ETL se cambiaron los nombres de las columnas de la siguiente manera:

* "EDAD": "edad",
* "DIABETES": "diabetes",
* "HOSPITALIZACIÓN ULTIMO MES": "hospitaliz_ult_mes",
* "PSA": "psa",
* "BIOPSIAS PREVIAS": "biopsias_prev",
* "VOLUMEN PROSTATICO": "vol_prostatico",
* "ANTIBIOTICO UTILIAZADO EN LA PROFILAXIS": "antibiotico_en_profilaxis",
* "NUMERO DE MUESTRAS TOMADAS": "nro_muestras",
* "CUP": "cup",
* "ENF. CRONICA PULMONAR OBSTRUCTIVA": "epoc",
* "BIOPSIA": "biopsia",
* "NUMERO DE DIAS POST BIOPSIA EN QUE SE PRESENTA LA COMPLICACIÓN INFECCIOSA": "nro_dias_con_infecc",
* "FIEBRE": "fiebre",
* "ITU": "itu",
* "TIPO DE CULTIVO": "tipo_cultivo",
* "AGENTE AISLADO": "agente_aislado",
* "PATRON DE RESISTENCIA": "patron_resistencia",
* "HOSPITALIZACION": "hospitalizacion",
* "DIAS HOSPITALIZACION MQ": "dias_hosp_mq",
* "DIAS HOSPITALIZACIÓN UPC": "dias_hosp_upc"