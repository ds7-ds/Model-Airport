# Website Design

## Menu

* Located on top of website

* Always visible regardless of device and orientation

* Fixed size for all devices

## Pages

#### Opening

* Video of model airport in action

   * Uses FitVids.js to ensure video fits on screen for all devices

* Tab will contain only the video to keep project goal of minimalistic demands

#### Info

* Facts and figures about the model airport

   * Uses PureCSS Grid to display information

* Photo gallery

   * Images must be a fixed size like 1920x1080 or 1280x720 due to PureCSS Grid constraints and to be decided later

   * Photos must be intriguing and helpful

* Inventory

   * Iframe container that links to inventory on GitHub

* Budget

   * Iframe container that links to budget on GitHub

#### Controller

###### Login

* To access the controller, users must first log in with username and password

###### Tutorial

* Gives user tips before using the webcam page

* TBD when Webcam page is made

###### Webcam

* Contains the live stream of the airport on top

   * Currently unknown as to what software/devices to use for webcam

      * Windows Phone ???

      * Raspberry Pi camera ???

      * IP Camera with web stream availability ???

      * Laptop ???

* Below the webcam stream is the message box where ATC commands are inputted

* Below the input box is the Send button (May be removed with automatic sending in the future)

## Website Visual

``
*************************************************************************************************
*            Video               *             Info            *                RC              *
*                                ****************************************************************
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                         Tab Content                                           *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*                                                                                               *
*************************************************************************************************
``

## Libraries

#### Links

* https://material.io/

* https://purecss.io/

* https://github.com/davatron5000/FitVids.js/