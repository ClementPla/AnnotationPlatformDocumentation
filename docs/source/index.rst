.. AnnotationPlatformDocumentation documentation master file, created by
   sphinx-quickstart on Wed Nov  4 10:45:26 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.




***************************************************************************
Welcome to the Retinal Annotation Project's!
***************************************************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What's our project?
========================
This project emerges from a collaboration between the Hospital Maisonneuve-Rosemont (**HMR**), Quebec Artificial Intelligence Institute (**Mila**)​, Diabetes Action Canada (**DAC**) and our team at the LIV4D laboratory in Polytechnique Montréal.

* Our goal is to collect a large annotated database of fundus images in order to train machine learning algorithms to predict early stage of diabetic retinopathy. 

* Specifically, we want to investigate deep-learning based solutions to facilitate screening of early DR onset and increase the capacity of telemedicine programs.

* **In practice**, this means overcome the technical challenges preventing state of the art screening models from being successfully applied in this context.

* To facilitate the communication between retinal specialists and our computer vision team, we have launched an online platform developed to collect and annotate retinal images.

.. image:: images/general_intro_image.png
   :width: 800

   
The core features of the software are:

* It's a web-based application​, you don't have to install anything
* The retinal images are anonymized and stored securely on an institutional server​
* It allows the labelling of biomarkers & disease grading.
* Images are already pre-annotated using our imperfect algorithms. The goal of the medical is to verify and correct the annotations.

An accurate labelling of biomarkers is essential to train segmentation models that learn to replicate the training samples and to generalize on new images. This segmentation task (ie: identification of local biomarkers in images such as lesions or anatomical structures) is a first step in a more global pipeline that will lead eventually to the automatic grading of diabetic retinopathy in fundus images. 

In the first phase of the project, we are collecting biomarkers annotations on a publicly available database: Messidor_.

.. _Messidor: http://www.adcis.net/fr/logiciels-tiers/messidor2-fr/

With the agreement of the owners of the database, we plan to release the biomarkers labels, to allow other labs to pursue their research on fundus images. Given the scarcity of such type of data, we believe this will be an important contribution.

So far, 200 images from Messidor database have been annotated by 8 experts, for a total of 12 biomarkers. Example of such annotations can be seen at:
    
Website map
============

* **Getting started** 
    Not familiar with the platform yet? Check out this tutorial:
    :doc:`Quick start </intro/getting_started>`

* **Looking for a shortcut?**
    :doc:`Lists of shortcuts </guides/shortcuts>`
    
* **Some annotation examples**
    :doc:`Examples of annotations </annotations/example>`

* **Documentation**
    Looking for more details about a functionality?
    :doc:`Follow the guide </guides/guide>` or check out the links in the index below.

* **Current advances on our algorithms**
    :doc:`Preliminary results with our AI algorithms</AI/wip>`
        
* **Want to know more about our team?**
    :doc:`LIV4D</us>`   


Index
======
.. toctree::
      :maxdepth: 2
    
      /intro/getting_started
      /guides/guide
      /guides/shortcuts
      /AI/wip
      /us
   

