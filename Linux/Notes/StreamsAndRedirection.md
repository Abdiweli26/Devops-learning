# Streams and Redirection  

  

## Standard Output  

  

```bash  

ls > output.txt  

```  

  

## Standard Error  

  

```bash  

ls missingfile 2> errors.txt  

```  

  

## Redirect Both  

  

```bash  

command > output.txt 2>&1  

```  

  

## Discard Output  

  

```bash  

command > /dev/null  

```  

  

## Discard Everything  

  

```bash  

command > /dev/null 2>&1  

```  

  

## Pipe Output  

  

```bash  

ls -l | grep notes  

```  

``