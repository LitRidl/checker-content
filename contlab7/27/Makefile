EJUDGE_PREFIX_DIR ?= /mnt/c/Users/Karma/Desktop/ejudge2/ejudge/inst-ejudge
EJUDGE_CONTESTS_HOME_DIR ?= /home/judges
EJUDGE_LOCAL_DIR ?= /var/lib/ejudge
EJUDGE_SERVER_BIN_PATH ?= /home/ejudge/inst-ejudge/bin

CC = python
CFLAGS =
CLIBS =

EXECUTE = ${EJUDGE_PREFIX_DIR}/bin/ejudge-execute
EXECUTE_FLAGS =  --use-stdin --use-stdout --test-pattern=%03d.dat --corr-pattern=%03d.ans

NORMALIZE = ${EJUDGE_SERVER_BIN_PATH}/ej-normalize
NORMALIZE_FLAGS = --workdir=tests --test-pattern=%03d.dat --corr-pattern=%03d.ans

all : answers
check_settings : all normalize

normalize :
	${NORMALIZE} ${NORMALIZE_FLAGS} --all-tests

answers : solution.py
	${EXECUTE} ${EXECUTE_FLAGS} --update-corr --test-dir=tests --workdir=tests --all-tests solution.py

clean :
	rm -f *.o *.class *.exe *~ *.bak a.out *.dSYM solution
