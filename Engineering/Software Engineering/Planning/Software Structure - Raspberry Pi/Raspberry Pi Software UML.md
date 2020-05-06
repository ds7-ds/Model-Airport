# Raspberry Pi Software UML

```
    (On Start Up)
          |
          |
          v
*********************          *******************           ***********************
*                   *          *                 *           *                     *
*  ModelAirport.js  *<-------->*  ConnectATC.py  *           *  ServerLessMain.py  *
*     (Node.js)     *          *     (Python)    *           *       (Python)      *
*                   *          *                 *           *                     *
*********************          *******************           ***********************
         ^                              |                                |
         |                              |
         v                              |                                |
(Connection to Server)                  |
                                        |                                |
                                        v
                            ************************                     |
                            *                      *
                            *  ModelAirportATC.py  *<- - - - - - - - - - +
                            *       (Python)       *
                            *                      *
                            ************************
                                        |
                                        |
                                        |
                                        |
                                        |
                                        v
                           ***************************          ***************************
                           *                         *          *                         *
                           *  ModelAirportImager.py  *--------->*  ModelAirportLogger.py  *
                           *        (Python)         *          *         (Python)        *
                           *                         *          *                         *
                           ***************************          ***************************
                                        |
                                        |
                                        |
                                        |
                                        |
                                        v
                           *************************
                           *                       *
                           *  ModelAirportGPIO.py  *
                           *        (Python)       *
                           *                       *
                           *************************
```