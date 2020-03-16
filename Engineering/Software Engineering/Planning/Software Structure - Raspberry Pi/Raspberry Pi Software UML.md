# Raspberry Pi Software UML

```
    (On Start Up)
          |
          |
          v
*********************          *******************
*                   *          *                 *
*  ModelAirport.js  *<-------->*  ConnectGTC.py  *
*     (Node.js)     *          *     (Python)    *
*                   *          *                 *
*********************          *******************
                                        |
                                        |
                                        |
                                        |
                                        |
                                        v
                            ************************
                            *                      *
                            *  ModelAirportGTC.py  *
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