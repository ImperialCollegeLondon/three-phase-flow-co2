-- Generated [
-- Format      : Eclipse keywords (ASCII)
-- Exported by : Petrel 2024.4.0 Schlumberger
-- User name   : oa2414
-- Date        : Sunday, November 02 2025 22:20:18
-- Project     : Fractional_flow.pet
-- Generated ]

RPTSCHED                               -- Generated : Petrel
  SOIL SWAT SGAS FIP WELLS SSOL /

RPTRST                                 -- Generated : Petrel
  BASIC=3 FLOWS FREQ BG BO BW /

SKIP                                   -- Generated : Petrel
--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up

ENDSKIP                                -- Generated : Petrel

--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up


WELSPECS                               -- Generated : Petrel
--'PRODUCER' is the simulation well name used to describe flow from 'Producer'
--'GI' is the simulation well name used to describe flow from 'GI'
--
  PRODUCER PROD 600 1 1* OIL /
  GI GI 1 1 1* GAS /
  /

COMPDAT                                -- Generated : Petrel
  PRODUCER 600 1 1 1 OPEN 1* 13.4222 0.1905 500 0 1* Z 0.700874 /
  GI 1 1 1 1 OPEN 1* 13.4222 0.1905 500 0 1* Z 0.700874 /
  /

GRUPTREE                               -- Generated : Petrel
  WI FIELD /
  PROD FIELD /
  GI FIELD /
  /

WCONPROD                               -- Generated : Petrel
  PRODUCER 7* 324 /
  /

WCONINJE                               -- Generated : Petrel
  GI GAS 1* BHP 2* 326 /
  /

DATES                                  -- Generated : Petrel
  2 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  3 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  4 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  5 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  6 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  7 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  8 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  9 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  10 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  11 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  12 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  13 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  14 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  15 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  16 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  17 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  18 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  19 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  20 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  21 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  22 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  23 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  24 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  25 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  26 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  27 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  28 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  29 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  30 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  31 JAN 2025 /
  /

DATES                                  -- Generated : Petrel
  1 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  2 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  3 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  4 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  5 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  6 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  7 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  8 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  9 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  10 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  11 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  12 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  13 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  14 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  15 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  16 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  17 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  18 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  19 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  20 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  21 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  22 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  23 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  24 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  25 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  26 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  27 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  28 FEB 2025 /
  /

DATES                                  -- Generated : Petrel
  1 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  2 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  3 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  4 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  5 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  6 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  7 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  8 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  9 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  10 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  11 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  12 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  13 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  14 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  15 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  16 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  17 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  18 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  19 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  20 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  21 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  22 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  23 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  24 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  25 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  26 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  27 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  28 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  29 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  30 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  31 MAR 2025 /
  /

DATES                                  -- Generated : Petrel
  1 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  2 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  3 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  4 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  5 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  6 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  7 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  8 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  9 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  10 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  11 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  12 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  13 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  14 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  15 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  16 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  17 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  18 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  19 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  20 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  21 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  22 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  23 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  24 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  25 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  26 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  27 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  28 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  29 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  30 APR 2025 /
  /

DATES                                  -- Generated : Petrel
  1 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  2 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  3 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  4 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  5 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  6 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  7 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  8 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  9 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  10 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  11 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  12 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  13 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  14 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  15 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  16 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  17 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  18 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  19 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  20 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  21 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  22 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  23 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  24 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  25 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  26 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  27 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  28 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  29 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  30 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  31 MAY 2025 /
  /

DATES                                  -- Generated : Petrel
  1 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  2 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  3 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  4 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  5 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  6 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  7 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  8 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  9 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  10 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  11 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  12 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  13 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  14 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  15 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  16 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  17 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  18 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  19 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  20 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  21 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  22 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  23 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  24 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  25 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  26 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  27 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  28 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  29 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  30 JUN 2025 /
  /

DATES                                  -- Generated : Petrel
  1 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  2 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  3 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  4 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  5 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  6 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  7 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  8 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  9 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  10 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  11 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  12 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  13 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  14 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  15 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  16 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  17 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  18 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  19 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  20 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  21 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  22 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  23 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  24 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  25 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  26 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  27 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  28 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  29 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  30 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  31 JUL 2025 /
  /

DATES                                  -- Generated : Petrel
  1 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  2 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  3 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  4 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  5 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  6 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  7 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  8 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  9 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  10 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  11 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  12 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  13 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  14 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  15 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  16 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  17 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  18 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  19 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  20 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  21 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  22 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  23 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  24 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  25 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  26 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  27 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  28 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  29 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  30 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  31 AUG 2025 /
  /

DATES                                  -- Generated : Petrel
  1 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  2 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  3 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  4 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  5 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  6 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  7 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  8 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  9 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  10 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  11 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  12 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  13 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  14 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  15 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  16 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  17 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  18 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  19 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  20 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  21 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  22 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  23 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  24 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  25 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  26 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  27 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  28 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  29 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  30 SEP 2025 /
  /

DATES                                  -- Generated : Petrel
  1 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  2 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  3 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  4 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  5 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  6 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  7 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  8 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  9 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  10 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  11 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  12 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  13 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  14 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  15 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  16 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  17 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  18 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  19 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  20 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  21 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  22 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  23 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  24 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  25 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  26 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  27 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  28 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  29 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  30 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  31 OCT 2025 /
  /

DATES                                  -- Generated : Petrel
  1 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  2 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  3 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  4 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  5 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  6 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  7 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  8 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  9 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  10 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  11 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  12 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  13 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  14 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  15 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  16 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  17 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  18 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  19 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  20 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  21 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  22 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  23 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  24 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  25 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  26 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  27 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  28 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  29 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  30 NOV 2025 /
  /

DATES                                  -- Generated : Petrel
  1 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  2 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  3 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  4 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  5 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  6 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  7 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  8 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  9 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  10 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  11 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  12 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  13 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  14 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  15 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  16 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  17 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  18 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  19 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  20 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  21 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  22 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  23 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  24 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  25 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  26 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  27 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  28 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  29 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  30 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  31 DEC 2025 /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  2 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  3 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  4 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  5 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  6 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  7 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  8 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  9 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  10 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  11 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  12 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  13 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  14 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  15 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  16 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  17 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  18 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  19 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  20 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  21 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  22 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  23 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  24 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  25 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  26 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  27 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  28 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  29 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  30 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  31 JAN 2026 /
  /

DATES                                  -- Generated : Petrel
  1 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  2 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  3 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  4 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  5 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  6 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  7 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  8 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  9 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  10 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  11 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  12 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  13 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  14 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  15 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  16 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  17 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  18 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  19 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  20 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  21 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  22 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  23 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  24 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  25 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  26 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  27 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  28 FEB 2026 /
  /

DATES                                  -- Generated : Petrel
  1 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  2 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  3 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  4 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  5 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  6 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  7 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  8 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  9 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  10 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  11 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  12 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  13 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  14 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  15 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  16 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  17 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  18 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  19 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  20 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  21 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  22 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  23 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  24 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  25 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  26 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  27 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  28 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  29 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  30 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  31 MAR 2026 /
  /

DATES                                  -- Generated : Petrel
  1 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  2 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  3 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  4 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  5 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  6 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  7 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  8 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  9 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  10 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  11 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  12 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  13 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  14 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  15 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  16 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  17 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  18 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  19 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  20 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  21 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  22 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  23 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  24 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  25 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  26 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  27 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  28 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  29 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  30 APR 2026 /
  /

DATES                                  -- Generated : Petrel
  1 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  2 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  3 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  4 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  5 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  6 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  7 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  8 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  9 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  10 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  11 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  12 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  13 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  14 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  15 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  16 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  17 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  18 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  19 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  20 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  21 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  22 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  23 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  24 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  25 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  26 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  27 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  28 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  29 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  30 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  31 MAY 2026 /
  /

DATES                                  -- Generated : Petrel
  1 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  2 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  3 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  4 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  5 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  6 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  7 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  8 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  9 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  10 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  11 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  12 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  13 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  14 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  15 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  16 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  17 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  18 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  19 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  20 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  21 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  22 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  23 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  24 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  25 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  26 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  27 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  28 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  29 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  30 JUN 2026 /
  /

DATES                                  -- Generated : Petrel
  1 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  2 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  3 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  4 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  5 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  6 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  7 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  8 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  9 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  10 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  11 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  12 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  13 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  14 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  15 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  16 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  17 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  18 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  19 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  20 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  21 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  22 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  23 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  24 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  25 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  26 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  27 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  28 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  29 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  30 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  31 JUL 2026 /
  /

DATES                                  -- Generated : Petrel
  1 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  2 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  3 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  4 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  5 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  6 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  7 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  8 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  9 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  10 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  11 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  12 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  13 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  14 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  15 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  16 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  17 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  18 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  19 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  20 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  21 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  22 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  23 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  24 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  25 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  26 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  27 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  28 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  29 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  30 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  31 AUG 2026 /
  /

DATES                                  -- Generated : Petrel
  1 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  2 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  3 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  4 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  5 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  6 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  7 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  8 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  9 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  10 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  11 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  12 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  13 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  14 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  15 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  16 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  17 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  18 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  19 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  20 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  21 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  22 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  23 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  24 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  25 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  26 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  27 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  28 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  29 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  30 SEP 2026 /
  /

DATES                                  -- Generated : Petrel
  1 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  2 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  3 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  4 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  5 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  6 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  7 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  8 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  9 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  10 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  11 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  12 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  13 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  14 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  15 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  16 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  17 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  18 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  19 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  20 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  21 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  22 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  23 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  24 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  25 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  26 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  27 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  28 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  29 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  30 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  31 OCT 2026 /
  /

DATES                                  -- Generated : Petrel
  1 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  2 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  3 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  4 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  5 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  6 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  7 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  8 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  9 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  10 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  11 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  12 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  13 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  14 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  15 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  16 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  17 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  18 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  19 NOV 2026 /
  /

DATES                                  -- Generated : Petrel
  19 NOV 2026 '02:00:00' /
  /

