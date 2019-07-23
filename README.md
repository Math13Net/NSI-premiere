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
* faire valider par le professeur
* créer votre projet sur Trello pour gérer le projet
(inviter votre professeur - il pourra voir ce que vous faites et vous accompagner dans votre démarche)
* pour un projet Raspberry en lien avec un chercheur de l'université de Bordeaux - contacter votre professeur directement


---------------------------------------------------------------------------------------------------------------------------
### <a name="projet1"></a> Projet Bloc 1 : Langages et programmation (premier trimeste)

#### Représentation de l’information

- expliquer simplement 0.1 + 0.2 != 0.3 puis rédiger un texte scientifique associé (ppt ou latex)
- créer un convertiseur permettant de changer de base de numérotation
- compression de données
- échantillonnage
- nombres flottants (e.g, visualisation des erreurs)
- chaînes de caractères
#### Programmation
- qq idées : [FUN python](https://projects.raspberrypi.org/en/projects?software%5B%5D=python) ou [SMILE](https://culturemath.ens.fr/category/generalites-270)
- simulation fonctionnelle d'une file d'attente (traiter différents cas ou exploiter en profomdeur une situation réelle)
- compréhension de listes
- tranches / Slices
- interface graphique (simple)
- modéliser une étude sur le monopoly - [monopoly](https://www.youtube.com/watch?v=KHPbaIFGZTE) - un peu dur ...
#### Web
- créer un site web pour une association - un club - une passion ...
- créer une site internet expliquant le fonctionnement des filtres sur une image avec quelques exemples (web + python)
- persistance des données côté client (e.g., cookies)
- mécanismes de caches
- envoie de données au serveur (e.g., formulaires, paramètres)
- validation des données d’un formulaire
- adaptation au média (e.g., responsive design)
- gestion des évènements dans le DOM (e.g., event bubbling and capturing)
- d'autres idées : qq idées : [FUN web](https://projects.raspberrypi.org/en/projects/?software[]=html-css-javascript)

---------------------------------------------------------------------------------------------------------------------------
### <a name="projet2"></a> Projet Bloc 2 : Machines et réseaux (deuxieme trimestre)
- grâce à une machine virtuelle, mettre une installation spécifique, puis faire des tests
- analyse dune trame ping (CiscoPaquetTracer - WireShark)
- creation d'un reseau double (avec router) - WireShark
- Raspberry Pi+ Node-Red : IoT Control Center with Node-RED
- projet Raspberry Pi + + Arduino + Node-Red
- allumage led (direct, via GPIO, via server web, via Node-Red)
- création d'un google home via raspberry pi (micro et enceinte : question puis réponse)
- ...
- Décomposition du code JavaScript côté client

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
  
  
  
  
