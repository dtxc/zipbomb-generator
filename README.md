# zipbomb-generator

the amount of layers should be less or equal than the amount of files per layer

and here are some formulas you might need:

$$\text{total extracted size}=\text{dd buffer}\times (\text{files per layer})^{\text{layers}}$$

$$\text{zip generation time}\approx\frac{\text{dd buffer}}{(\text{write speed})/5.12}+\sum_{k=1}^{\text{layers}}\frac{\text{dd buffer}}{1024^k},\\,\text{files per layer}\ge\text{layers}$$

$$\text{space required}\approx\text{files per layer}\times\frac{\text{dd buffer}}{1024}$$

