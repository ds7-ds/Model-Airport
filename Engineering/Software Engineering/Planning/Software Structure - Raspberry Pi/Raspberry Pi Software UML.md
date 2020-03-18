# Raspberry Pi Software UML

```
    (On Start Up)
          |
          |
          v
*********************          *******************           ***********************
*                   *          *                 *           *                     *
*  ModelAirport.js  *<-------->*  ConnectGTC.py  *           *  ServerLessMain.py  *
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
                            *  ModelAirportGTC.py  *<- - - - - - - - - - +
                            *       (Python)       *
                            *                      *
                            ************************
                                        |
                                        |
                                        |
                                        |
                                        |
                                        v
                           **************************          ***************************
                           *                        *          *                         *
                           *  ModelAirportGraph.py  *--------->*  ModelAirportLogger.py  *
                           *        (Python)        *          *         (Python)        *
                           *                        *          *                         *
                           **************************          ***************************
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