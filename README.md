# NSI-premiere

[Magic Problem Solver Algorithm ;))](https://proftomcrick.com/2011/04/26/feynman-problem-solving-algorithm/)

<a href="https://www.youtube.com/watch?v=gpJvvH8JFn4" target="_blank"><img src="https://github.com/Math13Net/NSI-premiere/blob/master/nsi.jpg" alt="NSI Première" width="120" height="90" border="10" /></a>

## [Programme officiel BO NSI Première](https://github.com/Math13Net/NSI-premiere/blob/master/programme-nsi-premiere.pdf)

## [Progression NSI premiere 2019-2020](#sommaire)

## [Projets pour le NSI premiere](#projet)

## [Références](#reference)

------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

## <a name="sommaire"></a> Progression Première NSI
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

### Chapitre 1 : PROGRAMMATION - PROJET - DONNEES
#### 1.1 [Python 3](https://repl.it/)
  * Élements de base - Instructions conditionnelles et boucles - Fonctions
  * Spécification et tests - Modules et bibliothèques

#### 1.2 Programmation pour le Web
 * Le langage [HTML](https://repl.it/)
 * Le langage [CSS](https://repl.it/)
 * Mon premier site Web

#### 1.3 Gestion de projet - Délivrables
* [GitHub](https://github.com/GitHub/) / MarkDown - [Trello](https://trello.com/)
* mon premier doc sous [Latex](https://v2.overleaf.com/login)

#### 1.4 Représentation des Données
 ##### Types simples
  * Représentation numérique de l’information - Nombres entiers - Booléeens
  * Nombres réels - Textes
 ##### Types construits
  * N-uplets - Listes - Tableaux et matrices
  * Dictionnaires - Traitement de données en tables

#### [Mini projet trimestre 1](#projet1)


------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

### Chapitre 2 : MACHINES ET RESEAUX

#### 2.1 Machines
##### HardWare et Langage Bas niveau
  * Architecture matérielle - [VirtualBox sous linux](https://www.virtualbox.org/wiki/Downloads) : du disque dur au fichier
  * Circuit logique - [Simulateur Labri](http://dept-info.labri.fr/ENSEIGNEMENT/archi/circuits/blank-teacher.html)
  * Langage machine - [Simulateur Y86](http://dept-info.labri.fr/ENSEIGNEMENT/archi/js-y86/)
##### Systèmes d’exploitation et Terminal
  * Linux / Raspian
  * Windows
##### Arduino et Raspberry Pi
 * présentation et [différence](https://www.youtube.com/watch?v=c1R4TH6U9rc)
 * [Mon premier projet sous Arduino](https://www.youtube.com/playlist?list=PL0YfVdOGWSEQCIEZj_-dFsnClqyxqDmA_)
 * [Mon premier projet sous Raspberry Pi](https://www.youtube.com/watch?v=Ew54Q28Gk_Y)
  
#### 2.2 Communication et Architecture Réseau
 * Modèle OSI et protocole TCP/IP
 * Masque et adresse IP
 * [Wireshark](https://www.wireshark.org/) : analyse d'une trame ping
 * [Cisco Pasket Tracer](https://www.netacad.com/fr/courses/packet-tracer) : connection de deux réseaux via un router

#### 2.2 Interactions sur le Web
 * Repères - Hypertexte - Interactions avec HTML et [JavaScript](https://repl.it/)
 * Requêtes HTTP - Formulaires dans une page Web
 * [Node-Red](https://nodered.org/) - Mon premier flow

#### [Mini projet trimestre 2](#projet2)

------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

### Chapitre 3 : ALGORITHMES

#### 3.1 Algorithmes 1
 * Introduction - Les outils - Validité et coût
 * Parcours séquentiel - Recherche dichotomique

#### 3.2 Algorithmes 2
 * Algorithmes de tri - Algorithme des plus proches voisins - Algorithmes gloutons

#### [Mini projet trimestre 3](#projet3)


------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------


## <a name="projet"></a> Projets pour le NSI

---------------------------------------------------------------------------------------------------------------------------
### <a name="demarche"></a> Démarche
* constituer un groupe de 2 ou 3 ou 4 élèves
* faire son choix à la fin de la séance 1
* faire valider par le professeur (le thème est choisi par les élèves, le professeur évalue la faisabilité)
* créer votre projet sur Trello pour gérer le projet
(inviter votre professeur - il pourra voir ce que vous faites et vous accompagner dans votre démarche)
* pour un projet Raspberry en lien avec un chercheur de l'université de Bordeaux - contacter votre professeur directement


---------------------------------------------------------------------------------------------------------------------------
### <a name="projet1"></a> Projet Bloc 1 : Langages et programmation (premier trimeste)

#### Données
- expliquer simplement 0.1 + 0.2 != 0.3 puis rédiger un texte scientifique associé
- représentation d'un nombre dans différentes bases
- compression de données
- échantillonnage
- nombres flottants (e.g, visualisation des erreurs)
- chaînes de caractères
- manipulation d'images
- convertisseur de couleurs
- échantillonnage du son
- lecture / écriture dans un fichier
- nombres flottants
- ...
#### Programmation
- qq idées : [FUN python](https://projects.raspberrypi.org/en/projects?software%5B%5D=python) ou [SMILE](https://culturemath.ens.fr/category/generalites-270)
- simulation fonctionnelle d'une file d'attente (traiter différents cas ou exploiter en profomdeur une situation réelle)
- interface graphique
- modéliser une étude sur le monopoly - [monopoly](https://www.youtube.com/watch?v=KHPbaIFGZTE) - un peu dur ...
- cryptographie - loi de Benford
- éruptions volcaniques et prédiction
- compréhension de listes
- tranches / slices
- ...
#### Web
- créer un site web pour une association - un club - une passion ...
- créer une site internet expliquant le fonctionnement des filtres sur une image (web + python)
- persistance des données côté client (e.g., cookies)
- mécanismes de caches
- envoie de données au serveur (e.g., formulaires, paramètres)
- validation des données d’un formulaire
- adaptation au média (e.g., responsive design)
- gestion des évènements dans le DOM (e.g., event bubbling and capturing)
- d'autres idées : qq idées : [FUN web](https://projects.raspberrypi.org/en/projects/?software[]=html-css-javascript)
_ ...

---------------------------------------------------------------------------------------------------------------------------
### <a name="projet2"></a> Projet Bloc 2 : Machines et réseaux (deuxieme trimestre)

#### Machine
- grâce à une machine virtuelle, mettre une installation spécifique, puis faire des tests
- représentation binaire des entiers relatifs
- notion de test et de branchement conditionnel
- réalisation des boucles usuelles en assembleur (for, while, do-while)
- manipulation des tableaux
- la pile et l’appel de fonctions
- l’unité arithmétique et logique d’un processeur
- implémentation des registres dans un processeur
- captation d’une donnée numérique
- captation d’une donnée analogique
- fabrication et test d’un capteur
- intégration d’un capteur, filtre de Kalman
- contrôle d’un servo moteur asservi à un capteur donné (exemple : fermeture d’un volet quand la nuit tombe)
- création d’un dispositif multi-capteurs pour réaliser une fonction donnée (exemple : capteur de détection de son et de lumière, type système d’alarme)
- création d’un robot mobile autonome
- arbre de Noel à base de LEDs (clignotement)
- détecteur d’ouverture de porte
- système “fuyant” en présence de bruit/lumière

#### Réseau
- analyse dune trame ping (CiscoPaquetTracer - WireShark)
- creation d'un reseau double (avec router) - WireShark
- fiabilisation des communications : code détecteur d’erreurs. Du bit de parité (simple et double) au CRC
- fiabilisation des communications : du bit alterné au numéro de séquence TCP
- internet décentralisé et le routage
- paiement sécurisé sur Internet (HTTPS)
- encapsulation des protocoles : exemple de HTTP
- sous-réseaux IP
- IPv6

#### Web
- Raspberry Pi+ Node-Red : IoT Control Center with Node-RED
- projet Raspberry Pi + + Arduino + Node-Red
- allumage led (direct, via GPIO, via server web, via Node-Red)
- création d'un google home via raspberry pi (micro et enceinte : question puis réponse)
- ...
- décomposition du code JavaScript côté client


---------------------------------------------------------------------------------------------------------------------------
### <a name="projet3"></a> Projet Bloc 3 : Algorithmes (troisieme trimeste)
 1. Greddy

 2. Dijkstra

 3. TAF : programmer le Knapsack Problem (problème du sac à doc / panier du voleur) - dynamic processing (activités tableur)

  * ex 1 : plus grande chaîne de caractère commune (mesure de levensthein : https://fr.wikipedia.org/wiki/Distance_de_Levenshtein)

  * ex 2 : plus grand nombre de caractères commun

  4. Quicksort and QuickSort improved

   * https://yourbasic.org/golang/quicksort-optimizations/
   
  5. K-Nearest Neighbor - classification and regression

   * ex1 : taille et couleur des oranges

   * ex2 : goût des utilisateurs Netflix (5 critères par exemple)

   * ex3 : vente croissant(nbre), climat(beau/mauvais), jour semaine(sem/we)
   

------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

## <a name="reference"></a> Références exploitées

### Livres
  * [NSI - Serge Bays](https://www.editions-ellipses.fr/spcialit-numrique-sciences-informatiques-premire-nouveaux-programmes-p-13318.html)
  * [NSI - Balabonski, Conchon, Filliâtre, Nguyen](https://www.editions-ellipses.fr/spcialit-numrique-sciences-informatiques-premire-nouveaux-programmes-p-13318.html)
  
### Vidéos  
  * [Algorithms in Motion - Beau carnes](https://www.manning.com/livevideo/algorithms-in-motion)
  * [An Introduction to Web Development in HTML, CSS, and JavaScript - Camryn Williams, Cassidy Williams](https://www.oreilly.com/library/view/an-introduction-to/9781491923320/)
  
### Sites
 * [Site de David Roche](https://pixees.fr/informatiquelycee/n_site/)
 * [Math93.com NSI](https://www.math93.com/lycee/nsi-1ere.html)
  
  
  
  
