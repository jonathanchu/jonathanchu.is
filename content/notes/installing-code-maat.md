+++
title = "Installing Code Maat"
author = ["Jonathan Chu"]
date = 2026-01-21T00:00:00-04:00
draft = false
+++

## Overview {#overview}

Code Maat is a forensic analysis tool for version control data, created by Adam Tornhill (author of "Your Code as a Crime Scene"). It analyzes git logs to identify hotspots, temporal coupling, code age, and other metrics. These are my notes and install instructions as I got it setup on my local machine.

-   Repository: <https://github.com/adamtornhill/code-maat>
-   Book: "Your Code as a Crime Scene" by Adam Tornhill


## Installation {#installation}


### 1. Install Java {#1-dot-install-java}

Code Maat is a Clojure application packaged as a JAR file, so it requires Java.

```bash
brew install openjdk
```

Add to your shell profile (~/.zshrc or ~/.bashrc):

```bash
export PATH="$(brew --prefix)/opt/openjdk/bin:$PATH"
```

Or create a system-wide symlink:

```bash
sudo ln -sfn $(brew --prefix)/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
```

Verify installation:

```bash
java -version
```


### 2. Download Code Maat {#2-dot-download-code-maat}

```bash
mkdir -p ~/tools/code-forensics
cd ~/tools/code-forensics
curl -sL https://github.com/adamtornhill/code-maat/releases/download/v1.0.4/code-maat-1.0.4-standalone.jar -o code-maat.jar
```

Verify installation:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -h
```


### 3. Optional: Create an alias {#3-dot-optional-create-an-alias}

Add to your shell profile:

```bash
alias code-maat="java -jar ~/tools/code-forensics/code-maat.jar"
```


## Usage {#usage}


### Step 1: Generate Git Log {#step-1-generate-git-log}

Code Maat requires a specially formatted git log. Run this in your project directory:

```bash
git log --all --numstat --date=short \
  --pretty=format:'--%h--%ad--%aN' \
  --no-renames > gitlog.txt
```


### Step 2: Run Analysis {#step-2-run-analysis}

All commands assume you're in the project directory with `gitlog.txt`.


#### Change Frequency (Hotspots) {#change-frequency--hotspots}

Find files that change most often:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a revisions
```


#### Temporal Coupling {#temporal-coupling}

Find files that change together:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a coupling
```


#### Authors / Ownership {#authors-ownership}

Who changed what:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a authors
```

Primary author per file:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a entity-ownership
```


#### Code Age {#code-age}

When files were last changed:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a age
```


#### Code Churn {#code-churn}

Lines added/removed per file:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a abs-churn
```


#### Summary {#summary}

Repository overview:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a summary
```


## Available Analyses {#available-analyses}

| Analysis         | Description                     |
|------------------|---------------------------------|
| revisions        | Change frequency per file       |
| coupling         | Temporal coupling between files |
| authors          | Who changed what                |
| entity-ownership | Primary author per file         |
| entity-effort    | Effort distribution             |
| age              | Code age                        |
| abs-churn        | Lines added/removed             |
| author-churn     | Churn per author                |
| communication    | Communication patterns          |
| summary          | Repository overview             |


## Output &amp; Visualization {#output-and-visualization}

Code Maat outputs CSV to stdout. Save to a file:

```bash
java -jar ~/tools/code-forensics/code-maat.jar -l gitlog.txt -c git2 -a revisions > revisions.csv
```

Tornhill provides D3.js visualization templates at:
<https://github.com/adamtornhill/code-maat#visualization>


## Quick Analysis Script {#quick-analysis-script}

One-liner to generate log and run all common analyses:

```bash
#!/bin/bash
# Run from your project directory

MAAT="java -jar ~/tools/code-forensics/code-maat.jar"
OUTDIR="code-forensics-output"

mkdir -p $OUTDIR

# Generate git log
git log --all --numstat --date=short \
  --pretty=format:'--%h--%ad--%aN' \
  --no-renames > $OUTDIR/gitlog.txt

# Run analyses
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a revisions > $OUTDIR/revisions.csv
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a coupling > $OUTDIR/coupling.csv
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a authors > $OUTDIR/authors.csv
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a age > $OUTDIR/age.csv
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a abs-churn > $OUTDIR/churn.csv
$MAAT -l $OUTDIR/gitlog.txt -c git2 -a summary > $OUTDIR/summary.csv

echo "Results saved to $OUTDIR/"
```


## Uninstall {#uninstall}

To remove Code Maat:

```bash
rm -rf ~/tools/code-forensics
```

To remove Java (if no longer needed):

```bash
brew uninstall openjdk
```
