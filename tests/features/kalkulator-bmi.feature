#language: pl

Właściwość: Kalkulator obliczający wskaźnik masy ciała (BMI)
  Jako trener osobisty
  chcę znać wskaźnik masy ciała (BMI) moich klientów
  tak, żebym mógł zaproponować im odpowiednią dietę i ćwiczenia

  Założenia:
    Zakładając że uruchomiłem aplikację

  Szablon scenariusza: Obliczanie wskaźnika BMI
    Jeżeli na stronie aplikacji wpiszę <WZROST> w pole wzrost
    I wpiszę <WAGA> w pole waga
    I nacisnę przycisk Oblicz
    Wtedy powinienem zobaczyć <BMI_LICZBOWO > jako wartość numeryczną BMI
    I <BMI_SŁOWNIE> jako kategorię przedziału BMI

  Przykłady:
    |WZROST |WAGA |BMI_LICZBOWO |BMI_SŁOWNIE  |
    |170    |50   |17.3         |Niedowaga    |
    |181    |80   |24.4         |Waga normalna|
    |180    |90   |27.8         |Nadwaga      |
    |175    |100  |32.7         |Otyłość      |
