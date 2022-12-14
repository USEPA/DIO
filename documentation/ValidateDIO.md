## Load the RDS of the built model

## Validate the Model

Load useeior to get access to built-in validation functions.

Validate that commodity output can be recalculated (within 1%) with the
model total requirements matrix (L) and demand vector (y) for US
production

``` r
library(useeior)
econval <- compareOutputandLeontiefXDemand(DIO, tolerance = 0.01)
print(paste("Number of sectors passing:",econval$N_Pass))
```

    ## [1] "Number of sectors passing: 409"

``` r
print(paste("Number of sectors failing:",econval$N_Fail))
```

    ## [1] "Number of sectors failing: 2"

``` r
print(paste("Sectors failing:", paste(econval$Failure$rownames, collapse = ", ")))
```

    ## [1] "Sectors failing: S00402/US, S00300/US"

Validate that flow totals by commodity (E_c) can be recalculated (within
1%) using the model satellite matrix (B), market shares matrix (V_n),
total requirements matrix (L), and demand vector (y) for US production

``` r
modelval <- compareEandLCIResult(DIO, tolerance = 0.01)
print(paste("Number of flow totals by commodity passing:",modelval$N_Pass))
```

    ## [1] "Number of flow totals by commodity passing: 2030751"

``` r
print(paste("Number of flow totals by commodity failing:",modelval$N_Fail))
```

    ## [1] "Number of flow totals by commodity failing: 0"

``` r
#print(paste("Sectors failing:", paste(modelval$Failure$variable, collapse = ", ")))
```

Validate that commodity output can be recalculated (within 1%) with
model total domestic requirements matrix (L_d) and model demand (y) for
US production

``` r
econval <- compareOutputandLeontiefXDemand(DIO,use_domestic=TRUE, tolerance = 0.01)
print(paste("Number of sectors passing:",econval$N_Pass))
```

    ## [1] "Number of sectors passing: 409"

``` r
print(paste("Number of sectors failing:",econval$N_Fail))
```

    ## [1] "Number of sectors failing: 2"

``` r
print(paste("Sectors failing:", paste(econval$Failure$rownames, collapse = ", ")))
```

    ## [1] "Sectors failing: S00402/US, S00300/US"

Validate that commodity output are properly transformed to industry
output via MarketShare

``` r
q_x_val <- compareCommodityOutputXMarketShareandIndustryOutputwithCPITransformation(DIO, tolerance = 0.01)
print(paste("Number of flow totals by commodity passing:",q_x_val$N_Pass))
```

    ## [1] "Number of flow totals by commodity passing: 409"

``` r
print(paste("Number of flow totals by commodity failing:",q_x_val$N_Fail))
```

    ## [1] "Number of flow totals by commodity failing: 2"

``` r
print(paste("Sectors with flow totals failing:", paste(q_x_val$Failure$rownames, collapse = ", ")))
```

    ## [1] "Sectors with flow totals failing: S00402/US, S00300/US"

Validate that commodity output equals to domestic use plus production
demand

``` r
q_val <- compareCommodityOutputandDomesticUseplusProductionDemand(DIO, tolerance = 0.01)
print(paste("Number of flow totals by commodity passing:",q_val$N_Pass))
```

    ## [1] "Number of flow totals by commodity passing: 410"

``` r
print(paste("Number of flow totals by commodity failing:",q_val$N_Fail))
```

    ## [1] "Number of flow totals by commodity failing: 1"

``` r
print(paste("Sectors with flow totals failing:", paste(q_val$Failure$rownames, collapse = ", ")))
```

    ## [1] "Sectors with flow totals failing: S00300/US"
