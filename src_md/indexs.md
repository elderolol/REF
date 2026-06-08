---
# REF_self_holding — IL Logic Map
**CPU:** QCPU (Q mode) Q03UDV
**Total Steps:** 687
**Blocks:** 6
**Generated:** 2026-06-08
---

## Block List
| # | Name | Steps | Condition Device | Action Count |
|---|------|-------|-----------------|--------------|
| 1 | BARCODE COPY L1 | 1–2 |  | 2 |
| 2 | BARCODE COPY L2 | 4–5 |  | 2 |
| 3 | L1 MODEL LOOKUP | 7–256 | LD M520, LD M520, LD M520 ... (+47) | 200 |
| 4 | L2 MODEL LOOKUP | 258–507 | LD M520, LD M520, LD M520 ... (+47) | 200 |
| 5 | BARCODE CLEAR | 509–532 | LD M107, LD M520, LD M107 | 21 |
| 6 | DISPLAY CORRECTION | 534–687 | LD M0, LD M0, LD M0 ... (+49) | 102 |

## Block Detail

### Block 1: BARCODE COPY L1 (Step 1–2)

**Trigger Condition:**

**Actions:**
- LD> D6980
- BMOV D6980

### Block 2: BARCODE COPY L2 (Step 4–5)

**Trigger Condition:**

**Actions:**
- LD> D7980
- BMOV D7980

### Block 3: L1 MODEL LOOKUP (Step 7–256)

**Trigger Condition:**
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- LDD>= D7000
- ANDD= D7001
- MOV K1
- LDD>= D7000
- ANDD= D7001
- MOV K2
- LDD>= D7000
- ANDD= D7001
- MOV K3
- LDD>= D7000
- ANDD= D7001
- MOV K4
- LDD>= D7000
- ANDD= D7001
- MOV K5
- LDD>= D7000
- ANDD= D7001
- MOV K6
- LDD>= D7000
- ANDD= D7001
- MOV K7
- LDD>= D7000
- ANDD= D7001
- MOV K8
- LDD>= D7000
- ANDD= D7001
- MOV K9
- LDD>= D7000
- ANDD= D7001
- MOV K10
- LDD>= D7000
- ANDD= D7001
- MOV K11
- LDD>= D7000
- ANDD= D7001
- MOV K12
- LDD>= D7000
- ANDD= D7001
- MOV K13
- LDD>= D7000
- ANDD= D7001
- MOV K14
- LDD>= D7000
- ANDD= D7001
- MOV K15
- LDD>= D7000
- ANDD= D7001
- MOV K16
- LDD>= D7000
- ANDD= D7001
- MOV K17
- LDD>= D7000
- ANDD= D7001
- MOV K18
- LDD>= D7000
- ANDD= D7001
- MOV K19
- LDD>= D7000
- ANDD= D7001
- MOV K20
- LDD>= D7000
- ANDD= D7001
- MOV K21
- LDD>= D7000
- ANDD= D7001
- MOV K22
- LDD>= D7000
- ANDD= D7001
- MOV K23
- LDD>= D7000
- ANDD= D7001
- MOV K24
- LDD>= D7000
- ANDD= D7001
- MOV K25
- AND= D0
- DMOV D301
- D+ D303
- DMOV D305
- D+ D307
- AND= D0
- DMOV D310
- D+ D312
- DMOV D314
- D+ D316
- AND= D0
- DMOV D319
- D+ D321
- DMOV D323
- D+ D325
- AND= D0
- DMOV D328
- D+ D330
- DMOV D332
- D+ D334
- AND= D0
- DMOV D337
- D+ D339
- DMOV D341
- D+ D343
- AND= D0
- DMOV D346
- D+ D348
- DMOV D350
- D+ D352
- AND= D0
- DMOV D355
- D+ D357
- DMOV D359
- D+ D361
- AND= D0
- DMOV D364
- D+ D366
- DMOV D368
- D+ D370
- AND= D0
- DMOV D373
- D+ D375
- DMOV D377
- D+ D379
- AND= D0
- DMOV D382
- D+ D384
- DMOV D386
- D+ D388
- AND= D0
- DMOV D391
- D+ D393
- DMOV D395
- D+ D397
- AND= D0
- DMOV D400
- D+ D402
- DMOV D404
- D+ D406
- AND= D0
- DMOV D409
- D+ D411
- DMOV D413
- D+ D415
- AND= D0
- DMOV D418
- D+ D420
- DMOV D422
- D+ D424
- AND= D0
- DMOV D427
- D+ D429
- DMOV D431
- D+ D433
- AND= D0
- DMOV D436
- D+ D438
- DMOV D440
- D+ D442
- AND= D0
- DMOV D445
- D+ D447
- DMOV D449
- D+ D451
- AND= D0
- DMOV D454
- D+ D456
- DMOV D458
- D+ D460
- AND= D0
- DMOV D463
- D+ D465
- DMOV D467
- D+ D469
- AND= D0
- DMOV D472
- D+ D474
- DMOV D476
- D+ D478
- AND= D0
- DMOV D481
- D+ D483
- DMOV D485
- D+ D487
- AND= D0
- DMOV D490
- D+ D492
- DMOV D494
- D+ D496
- AND= D0
- DMOV D499
- D+ D501
- DMOV D503
- D+ D505
- AND= D0
- DMOV D508
- D+ D510
- DMOV D512
- D+ D514
- AND= D0
- DMOV D517
- D+ D519
- DMOV D521
- D+ D523

### Block 4: L2 MODEL LOOKUP (Step 258–507)

**Trigger Condition:**
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M520
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- LDD>= D8000
- ANDD= D8001
- MOV K1
- LDD>= D8000
- ANDD= D8001
- MOV K2
- LDD>= D8000
- ANDD= D8001
- MOV K3
- LDD>= D8000
- ANDD= D8001
- MOV K4
- LDD>= D8000
- ANDD= D8001
- MOV K5
- LDD>= D8000
- ANDD= D8001
- MOV K6
- LDD>= D8000
- ANDD= D8001
- MOV K7
- LDD>= D8000
- ANDD= D8001
- MOV K8
- LDD>= D8000
- ANDD= D8001
- MOV K9
- LDD>= D8000
- ANDD= D8001
- MOV K10
- LDD>= D8000
- ANDD= D8001
- MOV K11
- LDD>= D8000
- ANDD= D8001
- MOV K12
- LDD>= D8000
- ANDD= D8001
- MOV K13
- LDD>= D8000
- ANDD= D8001
- MOV K14
- LDD>= D8000
- ANDD= D8001
- MOV K15
- LDD>= D8000
- ANDD= D8001
- MOV K16
- LDD>= D8000
- ANDD= D8001
- MOV K17
- LDD>= D8000
- ANDD= D8001
- MOV K18
- LDD>= D8000
- ANDD= D8001
- MOV K19
- LDD>= D8000
- ANDD= D8001
- MOV K20
- LDD>= D8000
- ANDD= D8001
- MOV K21
- LDD>= D8000
- ANDD= D8001
- MOV K22
- LDD>= D8000
- ANDD= D8001
- MOV K23
- LDD>= D8000
- ANDD= D8001
- MOV K24
- LDD>= D8000
- ANDD= D8001
- MOV K25
- AND= D32
- DMOV D551
- D+ D553
- DMOV D555
- D+ D557
- AND= D32
- DMOV D560
- D+ D562
- DMOV D564
- D+ D566
- AND= D32
- DMOV D569
- D+ D571
- DMOV D573
- D+ D575
- AND= D32
- DMOV D578
- D+ D580
- DMOV D582
- D+ D584
- AND= D32
- DMOV D587
- D+ D589
- DMOV D591
- D+ D593
- AND= D32
- DMOV D596
- D+ D598
- DMOV D600
- D+ D602
- AND= D32
- DMOV D605
- D+ D607
- DMOV D609
- D+ D611
- AND= D32
- DMOV D614
- D+ D616
- DMOV D618
- D+ D620
- AND= D32
- DMOV D623
- D+ D625
- DMOV D627
- D+ D629
- AND= D32
- DMOV D632
- D+ D634
- DMOV D636
- D+ D638
- AND= D32
- DMOV D641
- D+ D643
- DMOV D645
- D+ D647
- AND= D32
- DMOV D650
- D+ D652
- DMOV D654
- D+ D656
- AND= D32
- DMOV D659
- D+ D661
- DMOV D663
- D+ D665
- AND= D32
- DMOV D668
- D+ D670
- DMOV D672
- D+ D674
- AND= D32
- DMOV D677
- D+ D679
- DMOV D681
- D+ D683
- AND= D32
- DMOV D686
- D+ D688
- DMOV D690
- D+ D692
- AND= D32
- DMOV D695
- D+ D697
- DMOV D699
- D+ D701
- AND= D32
- DMOV D704
- D+ D706
- DMOV D708
- D+ D710
- AND= D32
- DMOV D713
- D+ D715
- DMOV D717
- D+ D719
- AND= D32
- DMOV D722
- D+ D724
- DMOV D726
- D+ D728
- AND= D32
- DMOV D731
- D+ D733
- DMOV D735
- D+ D737
- AND= D32
- DMOV D740
- D+ D742
- DMOV D744
- D+ D746
- AND= D32
- DMOV D749
- D+ D751
- DMOV D753
- D+ D755
- AND= D32
- DMOV D758
- D+ D760
- DMOV D762
- D+ D764
- AND= D32
- DMOV D767
- D+ D769
- DMOV D771
- D+ D773

### Block 5: BARCODE CLEAR (Step 509–532)

**Trigger Condition:**
- LD M107
- LD M520
- LD M107

**Actions:**
- OR M123
- OR M108
- OR M109
- OR M124
- OR M125
- OR M300
- FMOV K0
- FMOV K0
- MOV K0
- MOV K0
- MOV K0
- MOV K0
- OR M123
- OR M108
- OR M109
- OR M124
- OR M125
- OR M300
- ANB 
- RST D0
- RST D32

### Block 6: DISPLAY CORRECTION (Step 534–687)

**Trigger Condition:**
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0
- LD M0

**Actions:**
- DMOV D12
- AND= D0
- D+ D304
- AND= D0
- D+ D313
- AND= D0
- D+ D322
- AND= D0
- D+ D331
- AND= D0
- D+ D340
- AND= D0
- D+ D349
- AND= D0
- D+ D358
- AND= D0
- D+ D367
- AND= D0
- D+ D376
- AND= D0
- D+ D385
- AND= D0
- D+ D394
- AND= D0
- D+ D403
- AND= D0
- D+ D412
- AND= D0
- D+ D421
- AND= D0
- D+ D430
- AND= D0
- D+ D439
- AND= D0
- D+ D448
- AND= D0
- D+ D457
- AND= D0
- D+ D466
- AND= D0
- D+ D475
- AND= D0
- D+ D484
- AND= D0
- D+ D493
- AND= D0
- D+ D502
- AND= D0
- D+ D511
- AND= D0
- D+ D520
- DMOV D44
- AND= D32
- D+ D554
- AND= D32
- D+ D563
- AND= D32
- D+ D572
- AND= D32
- D+ D581
- AND= D32
- D+ D590
- AND= D32
- D+ D599
- AND= D32
- D+ D608
- AND= D32
- D+ D617
- AND= D32
- D+ D626
- AND= D32
- D+ D635
- AND= D32
- D+ D644
- AND= D32
- D+ D653
- AND= D32
- D+ D662
- AND= D32
- D+ D671
- AND= D32
- D+ D680
- AND= D32
- D+ D689
- AND= D32
- D+ D698
- AND= D32
- D+ D707
- AND= D32
- D+ D716
- AND= D32
- D+ D725
- AND= D32
- D+ D734
- AND= D32
- D+ D743
- AND= D32
- D+ D752
- AND= D32
- D+ D761
- AND= D32
- D+ D770

## Device Map
| Device | Type | SET Steps | RST Steps | OUT Steps | Read Steps |
|--------|------|-----------|-----------|-----------|------------|
| D0 | D |  | 1 |  | 50 |
| D12 | D |  |  |  | 1 |
| D301 | D |  |  |  | 1 |
| D303 | D |  |  |  | 1 |
| D304 | D |  |  |  | 1 |
| D305 | D |  |  |  | 1 |
| D307 | D |  |  |  | 1 |
| D310 | D |  |  |  | 1 |
| D312 | D |  |  |  | 1 |
| D313 | D |  |  |  | 1 |
| D314 | D |  |  |  | 1 |
| D316 | D |  |  |  | 1 |
| D319 | D |  |  |  | 1 |
| D32 | D |  | 1 |  | 50 |
| D321 | D |  |  |  | 1 |
| D322 | D |  |  |  | 1 |
| D323 | D |  |  |  | 1 |
| D325 | D |  |  |  | 1 |
| D328 | D |  |  |  | 1 |
| D330 | D |  |  |  | 1 |
| D331 | D |  |  |  | 1 |
| D332 | D |  |  |  | 1 |
| D334 | D |  |  |  | 1 |
| D337 | D |  |  |  | 1 |
| D339 | D |  |  |  | 1 |
| D340 | D |  |  |  | 1 |
| D341 | D |  |  |  | 1 |
| D343 | D |  |  |  | 1 |
| D346 | D |  |  |  | 1 |
| D348 | D |  |  |  | 1 |
| D349 | D |  |  |  | 1 |
| D350 | D |  |  |  | 1 |
| D352 | D |  |  |  | 1 |
| D355 | D |  |  |  | 1 |
| D357 | D |  |  |  | 1 |
| D358 | D |  |  |  | 1 |
| D359 | D |  |  |  | 1 |
| D361 | D |  |  |  | 1 |
| D364 | D |  |  |  | 1 |
| D366 | D |  |  |  | 1 |
| D367 | D |  |  |  | 1 |
| D368 | D |  |  |  | 1 |
| D370 | D |  |  |  | 1 |
| D373 | D |  |  |  | 1 |
| D375 | D |  |  |  | 1 |
| D376 | D |  |  |  | 1 |
| D377 | D |  |  |  | 1 |
| D379 | D |  |  |  | 1 |
| D382 | D |  |  |  | 1 |
| D384 | D |  |  |  | 1 |
| D385 | D |  |  |  | 1 |
| D386 | D |  |  |  | 1 |
| D388 | D |  |  |  | 1 |
| D391 | D |  |  |  | 1 |
| D393 | D |  |  |  | 1 |
| D394 | D |  |  |  | 1 |
| D395 | D |  |  |  | 1 |
| D397 | D |  |  |  | 1 |
| D400 | D |  |  |  | 1 |
| D402 | D |  |  |  | 1 |
| D403 | D |  |  |  | 1 |
| D404 | D |  |  |  | 1 |
| D406 | D |  |  |  | 1 |
| D409 | D |  |  |  | 1 |
| D411 | D |  |  |  | 1 |
| D412 | D |  |  |  | 1 |
| D413 | D |  |  |  | 1 |
| D415 | D |  |  |  | 1 |
| D418 | D |  |  |  | 1 |
| D420 | D |  |  |  | 1 |
| D421 | D |  |  |  | 1 |
| D422 | D |  |  |  | 1 |
| D424 | D |  |  |  | 1 |
| D427 | D |  |  |  | 1 |
| D429 | D |  |  |  | 1 |
| D430 | D |  |  |  | 1 |
| D431 | D |  |  |  | 1 |
| D433 | D |  |  |  | 1 |
| D436 | D |  |  |  | 1 |
| D438 | D |  |  |  | 1 |
| D439 | D |  |  |  | 1 |
| D44 | D |  |  |  | 1 |
| D440 | D |  |  |  | 1 |
| D442 | D |  |  |  | 1 |
| D445 | D |  |  |  | 1 |
| D447 | D |  |  |  | 1 |
| D448 | D |  |  |  | 1 |
| D449 | D |  |  |  | 1 |
| D451 | D |  |  |  | 1 |
| D454 | D |  |  |  | 1 |
| D456 | D |  |  |  | 1 |
| D457 | D |  |  |  | 1 |
| D458 | D |  |  |  | 1 |
| D460 | D |  |  |  | 1 |
| D463 | D |  |  |  | 1 |
| D465 | D |  |  |  | 1 |
| D466 | D |  |  |  | 1 |
| D467 | D |  |  |  | 1 |
| D469 | D |  |  |  | 1 |
| D472 | D |  |  |  | 1 |
| D474 | D |  |  |  | 1 |
| D475 | D |  |  |  | 1 |
| D476 | D |  |  |  | 1 |
| D478 | D |  |  |  | 1 |
| D481 | D |  |  |  | 1 |
| D483 | D |  |  |  | 1 |
| D484 | D |  |  |  | 1 |
| D485 | D |  |  |  | 1 |
| D487 | D |  |  |  | 1 |
| D490 | D |  |  |  | 1 |
| D492 | D |  |  |  | 1 |
| D493 | D |  |  |  | 1 |
| D494 | D |  |  |  | 1 |
| D496 | D |  |  |  | 1 |
| D499 | D |  |  |  | 1 |
| D501 | D |  |  |  | 1 |
| D502 | D |  |  |  | 1 |
| D503 | D |  |  |  | 1 |
| D505 | D |  |  |  | 1 |
| D508 | D |  |  |  | 1 |
| D510 | D |  |  |  | 1 |
| D511 | D |  |  |  | 1 |
| D512 | D |  |  |  | 1 |
| D514 | D |  |  |  | 1 |
| D517 | D |  |  |  | 1 |
| D519 | D |  |  |  | 1 |
| D520 | D |  |  |  | 1 |
| D521 | D |  |  |  | 1 |
| D523 | D |  |  |  | 1 |
| D551 | D |  |  |  | 1 |
| D553 | D |  |  |  | 1 |
| D554 | D |  |  |  | 1 |
| D555 | D |  |  |  | 1 |
| D557 | D |  |  |  | 1 |
| D560 | D |  |  |  | 1 |
| D562 | D |  |  |  | 1 |
| D563 | D |  |  |  | 1 |
| D564 | D |  |  |  | 1 |
| D566 | D |  |  |  | 1 |
| D569 | D |  |  |  | 1 |
| D571 | D |  |  |  | 1 |
| D572 | D |  |  |  | 1 |
| D573 | D |  |  |  | 1 |
| D575 | D |  |  |  | 1 |
| D578 | D |  |  |  | 1 |
| D580 | D |  |  |  | 1 |
| D581 | D |  |  |  | 1 |
| D582 | D |  |  |  | 1 |
| D584 | D |  |  |  | 1 |
| D587 | D |  |  |  | 1 |
| D589 | D |  |  |  | 1 |
| D590 | D |  |  |  | 1 |
| D591 | D |  |  |  | 1 |
| D593 | D |  |  |  | 1 |
| D596 | D |  |  |  | 1 |
| D598 | D |  |  |  | 1 |
| D599 | D |  |  |  | 1 |
| D600 | D |  |  |  | 1 |
| D602 | D |  |  |  | 1 |
| D605 | D |  |  |  | 1 |
| D607 | D |  |  |  | 1 |
| D608 | D |  |  |  | 1 |
| D609 | D |  |  |  | 1 |
| D611 | D |  |  |  | 1 |
| D614 | D |  |  |  | 1 |
| D616 | D |  |  |  | 1 |
| D617 | D |  |  |  | 1 |
| D618 | D |  |  |  | 1 |
| D620 | D |  |  |  | 1 |
| D623 | D |  |  |  | 1 |
| D625 | D |  |  |  | 1 |
| D626 | D |  |  |  | 1 |
| D627 | D |  |  |  | 1 |
| D629 | D |  |  |  | 1 |
| D632 | D |  |  |  | 1 |
| D634 | D |  |  |  | 1 |
| D635 | D |  |  |  | 1 |
| D636 | D |  |  |  | 1 |
| D638 | D |  |  |  | 1 |
| D641 | D |  |  |  | 1 |
| D643 | D |  |  |  | 1 |
| D644 | D |  |  |  | 1 |
| D645 | D |  |  |  | 1 |
| D647 | D |  |  |  | 1 |
| D650 | D |  |  |  | 1 |
| D652 | D |  |  |  | 1 |
| D653 | D |  |  |  | 1 |
| D654 | D |  |  |  | 1 |
| D656 | D |  |  |  | 1 |
| D659 | D |  |  |  | 1 |
| D661 | D |  |  |  | 1 |
| D662 | D |  |  |  | 1 |
| D663 | D |  |  |  | 1 |
| D665 | D |  |  |  | 1 |
| D668 | D |  |  |  | 1 |
| D670 | D |  |  |  | 1 |
| D671 | D |  |  |  | 1 |
| D672 | D |  |  |  | 1 |
| D674 | D |  |  |  | 1 |
| D677 | D |  |  |  | 1 |
| D679 | D |  |  |  | 1 |
| D680 | D |  |  |  | 1 |
| D681 | D |  |  |  | 1 |
| D683 | D |  |  |  | 1 |
| D686 | D |  |  |  | 1 |
| D688 | D |  |  |  | 1 |
| D689 | D |  |  |  | 1 |
| D690 | D |  |  |  | 1 |
| D692 | D |  |  |  | 1 |
| D695 | D |  |  |  | 1 |
| D697 | D |  |  |  | 1 |
| D698 | D |  |  |  | 1 |
| D6980 | D |  |  |  | 2 |
| D699 | D |  |  |  | 1 |
| D7000 | D |  |  |  | 25 |
| D7001 | D |  |  |  | 25 |
| D701 | D |  |  |  | 1 |
| D704 | D |  |  |  | 1 |
| D706 | D |  |  |  | 1 |
| D707 | D |  |  |  | 1 |
| D708 | D |  |  |  | 1 |
| D710 | D |  |  |  | 1 |
| D713 | D |  |  |  | 1 |
| D715 | D |  |  |  | 1 |
| D716 | D |  |  |  | 1 |
| D717 | D |  |  |  | 1 |
| D719 | D |  |  |  | 1 |
| D722 | D |  |  |  | 1 |
| D724 | D |  |  |  | 1 |
| D725 | D |  |  |  | 1 |
| D726 | D |  |  |  | 1 |
| D728 | D |  |  |  | 1 |
| D731 | D |  |  |  | 1 |
| D733 | D |  |  |  | 1 |
| D734 | D |  |  |  | 1 |
| D735 | D |  |  |  | 1 |
| D737 | D |  |  |  | 1 |
| D740 | D |  |  |  | 1 |
| D742 | D |  |  |  | 1 |
| D743 | D |  |  |  | 1 |
| D744 | D |  |  |  | 1 |
| D746 | D |  |  |  | 1 |
| D749 | D |  |  |  | 1 |
| D751 | D |  |  |  | 1 |
| D752 | D |  |  |  | 1 |
| D753 | D |  |  |  | 1 |
| D755 | D |  |  |  | 1 |
| D758 | D |  |  |  | 1 |
| D760 | D |  |  |  | 1 |
| D761 | D |  |  |  | 1 |
| D762 | D |  |  |  | 1 |
| D764 | D |  |  |  | 1 |
| D767 | D |  |  |  | 1 |
| D769 | D |  |  |  | 1 |
| D770 | D |  |  |  | 1 |
| D771 | D |  |  |  | 1 |
| D773 | D |  |  |  | 1 |
| D7980 | D |  |  |  | 2 |
| D8000 | D |  |  |  | 25 |
| D8001 | D |  |  |  | 25 |
| K0 | K |  |  |  | 6 |
| K1 | K |  |  |  | 2 |
| K10 | K |  |  |  | 2 |
| K11 | K |  |  |  | 2 |
| K12 | K |  |  |  | 2 |
| K13 | K |  |  |  | 2 |
| K14 | K |  |  |  | 2 |
| K15 | K |  |  |  | 2 |
| K16 | K |  |  |  | 2 |
| K17 | K |  |  |  | 2 |
| K18 | K |  |  |  | 2 |
| K19 | K |  |  |  | 2 |
| K2 | K |  |  |  | 2 |
| K20 | K |  |  |  | 2 |
| K21 | K |  |  |  | 2 |
| K22 | K |  |  |  | 2 |
| K23 | K |  |  |  | 2 |
| K24 | K |  |  |  | 2 |
| K25 | K |  |  |  | 2 |
| K3 | K |  |  |  | 2 |
| K4 | K |  |  |  | 2 |
| K5 | K |  |  |  | 2 |
| K6 | K |  |  |  | 2 |
| K7 | K |  |  |  | 2 |
| K8 | K |  |  |  | 2 |
| K9 | K |  |  |  | 2 |
| M0 | M |  |  |  | 102 |
| M107 | M |  |  |  | 2 |
| M108 | M |  |  |  | 2 |
| M109 | M |  |  |  | 2 |
| M123 | M |  |  |  | 2 |
| M124 | M |  |  |  | 2 |
| M125 | M |  |  |  | 2 |
| M300 | M |  |  |  | 2 |
| M520 | M |  |  |  | 51 |
