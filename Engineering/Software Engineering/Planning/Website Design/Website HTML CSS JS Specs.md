# Website HTML CSS JS Specs

Information on how the website should be designed and labels used to describe it

## Description

#### Website Structure

###### index.html

``
model-airport-app \(html\)
 |
 |-- model-airport-page-resources \(head\)
 |
 +-- model-airport-page \(body\)
      |
      |-- model-airport-tab-bar
      |    |
      |    +-- \(mdc-tab-bar...\)
      |
      +- model-airport-tab-content
          |
          |-- model-airport-video
          |    |
          |    +-- model-airport-video-container \(Used for FitVids.js\)
          |
          |-- model-airport-info
          |    |
          |    |-- model-airport-facts-and-figures
          |    |    |
          |    |    |-- model-airport-section-header
          |    |    |
          |    |    +-- \(PureCSS grid...\)  model-airport-grid-visual-small  model-airport-grid-caption-small
          |    |
          |    |-- model-airport-photo-gallery
          |    |    |
          |    |    |-- model-airport-section-header
          |    |    |
          |    |    +-- \(PureCSS grid...\)  model-airport-grid-visual-full  model-airport-grid-caption-small
          |    |
          |    |-- model-airport-inventory
          |    |    |
          |    |    |-- model-airport-section-header
          |    |    |
          |    |    +-- \(PureCSS grid...\)  model-airport-grid-visual-full  model-airport-grid-caption-small
          |    |
          |    |-- model-airport-budget
          |    |    |
          |    |    |-- model-airport-section-header
          |    |    |
          |    |    +-- \(PureCSS grid...\)  model-airport-grid-visual-full  model-airport-grid-caption-small
          |    |
          |    +-- model-airport-credits
          |         |
          |         |-- model-airport-section-header
          |         |
          |         +-- \(PureCSS grid...\)  model-airport-grid-caption-medium
          |
          +-- model-airport-rc
               |
               +-- model-airport-external-website \(iframe\)
``

###### login.html

``
model-airport-sub-app
 |
 |-- model-airport-page-resources
 |
 +-- model-airport-page
      |
      +-- model-airport-section-form
           |
           |-- model-airport-section-form-text-field
           |
           |-- model-airport-section-form-text-field
           |
           +-- model-airport-section-form-button
``

###### webcam.html

``
model-airport-sub-app
 |
 |-- model-airport-page-resources
 |
 +-- model-airport-page
      |
      +-- model-airport-section-webcam

``

###### blank.html

``
model-airport-sub-app
 |
 |-- model-airport-page-resources
 |
 +-- model-airport-page
      |
      +-- model-airport-section-header

``