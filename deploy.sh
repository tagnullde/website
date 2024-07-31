#!/bin/bash

hugo --cleanDestinationDir
git add .
git commit -a
git push origin main
