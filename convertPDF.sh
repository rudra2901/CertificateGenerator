#!/usr/bin/env bash

cd ~/CertificateGenerator/input/
list=(*.png)
for img in "${list[@]}"; do
    convert $img -quality 100 ~/CertificateGenerator/output/"$img".pdf
done

echo Success
