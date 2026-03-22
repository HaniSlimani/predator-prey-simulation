# Lien ressources bibliographiques

## 11/03/2024
### Yasmine
https://www.aktio.cc/ressources/risques-dereglement-climatique-entreprises

### Fernando

Explication pour la croissance des proies:    lorsque y'a moins de proies,alors il n'y aura pas assez de proies pour les prédateurs se nourrire. (Probablement,il y a la seléction naturelle qui intervient dans cela,qui a permis une coévolution des prédateurs et des proies.)

Si on continue d'exécuter notre modèle, on obtiendra un équilibre entre les prédateurs et les proies.

![image](https://github.com/ARE-Dynamic-G1-2024/climat_marche_financier/assets/159771245/3bcd37e8-f2d8-4afc-bc12-b15042921932)
![image](https://github.com/ARE-Dynamic-G1-2024/climat_marche_financier/assets/159771245/ac049576-1617-4a16-bd15-6bf62539804a)
![image](https://github.com/ARE-Dynamic-G1-2024/climat_marche_financier/assets/159771245/6645ae3d-59da-44b5-bd73-0c26289767f0)

https://accromath.uqam.ca/2013/05/des-predateurs-et-leurs-proies/#:~:text=%C3%80%20un%20certain%20niveau%20le,d'un%20certain%20%C3%A9quilibre%20dynamique.



Chaque population (de proie et de ses prédateurs) contrôle en quelque sorte la croissance de l'autre, autour d'un niveau d'équilibre
https://fr.wikipedia.org/wiki/%C3%89quilibres_pr%C3%A9dateurs-proies


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Phuong
https://read.oecd-ilibrary.org/environment/les-consequences-economiques-du-changement-climatique_9789264261082-fr#page1

OCDE. Les conséquences économiques du changement climatique. OECD, 2016. DOI.org (Crossref), https://doi.org/10.1787/9789264261082-fr.

J'ai trouvé une publication de l'OECD portant sur la modélisation du lien entre les effets du changement climatique et les activités économiques.
Dans ce document, ils ont parlé de "*la fonction de production*" (page 32) dont on peut s'inspirer pour notre projet. 
*La fonction de production* (L'image au-dessous) est une fonction qui prend les facteurs de production(travail et capital) comme inputs et ressortit un niveau de production maximale(la quantité de biens produite) associée à ces facteurs.


![image](https://github.com/ARE-Dynamic-G1-2024/climat_marche_financier/assets/152914256/84221e12-ac41-42b6-a6ac-d6429d9d3c3e)

Ensuite, j'ai trouvé quelques informations sur *la fonction de Cobb-Douglas* 

(La partie 1.a de https://www.maxicours.com/se/cours/la-fonction-de-production-et-l-accumulation-des-facteurs-de-production/#:~:text=La%20fonction%20de%20production%20se,K%20correspond%20au%20facteur%20capital.)

La formule est:
$$Q=f(\alpha K,\beta L)$$ 
où 
* $Q$ correspond au niveau de production
* $K$ à celui du capital
* $L$ à celui du travail
* $\alpha$ et $\beta$ correspondent à la répartition des revenus entre le travail et le capital (on utilise fréquemment $\beta = 1-\alpha$)

**Exemple**
  
  Si 60 % de la production provient du facteur capital et 40 % du facteur travail, alors la fonction est la suivante : $Q = f(K\times 0,6 , L\times 0,4)$. $α = 0,6$ et $β = 0,4$

  Enfin, j'ai quelques idées sur notre modèle:
  * Évaluer la production des pays
  * Créer une liste des pays, chacun va contenir les indices d'impactes climatique.
  * Utiliser la fonction de Cobb-Douglas
  * Créer une "grande" fonction appelé production() (correspondant à schelling()) qui calcule la production du pays dans un an par exemple.
  * production() va prendre $K$, $L$ et $\alpha$ comme paramètre
  * Écrire les fonctions pour calculer $K$ et $L$ (travail et capital) qui va prendre les impacts climatiques comme paramètre. Donc ces impacts vont affecter le travail et le capital, affecte donc la production
  * Écrire une fonction repartition() pour tirer aléatoirement $\alpha$
  * Utiliser les boucles de Python pour évaluer la production du pays après $n$ années (chaque tour du boucle represente un an)

https://oa.upm.es/47723/1/FRANCISCO_JOSE_FERNANDEZ_JORQUERA.pdf


Hani
1)Lien entre la concentration de co2 et la précipitation
https://www.quora.com/How-will-increased-atmospheric-CO2-concentration-affect-global-precipitation#:~:text=Increased%20Evaporation%3A%20Higher%20atmospheric%20CO2,of%20precipitation%20in%20some%20regions.

2)Deux études qui parlent directement du sujet
https://oa.upm.es/47723/1/FRANCISCO_JOSE_FERNANDEZ_JORQUERA.pdf

https://www.unescap.org/sites/default/files/5.%20The-Impact-of-Climate-Change-on-the-Agricultural-Sector.pdf

https://www.oecd.org/agriculture/ministerial/documents/Agriculture%20and%20Climate%20Change.pdf

https://www.manage.gov.in/studymaterial/CCA-E.pdf

https://core.ac.uk/download/pdf/151493831.pdf

https://ged.univ-rennes1.fr/nuxeo/site/esupversions/5f2a548a-008e-4503-acf7-7cf93b6b591d?inline



**Recherche sur le nouveau sujet**

https://www.researchgate.net/publication/221911917_Studies_on_Population_Dynamics_Using_Cellular

https://www.researchgate.net/publication/270451971_A_Survey_on_Cellular_Automata_and_Its_Applications

https://www.researchgate.net/publication/330254585_Cellular_Automata_and_Its_Applications

https://www.researchgate.net/publication/303683438_Lotka_Volterra_and_their_model
