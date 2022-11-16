# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ..
BUILDDIR      = ../builddoc

TOHTML			= html
FORMAT	= html
TOPDF	= latexpdf
TOSINGLE = singlehtml

SRC = /doc

.PHONY: help all src

help:
	@echo ''
	@echo 'Usage:'
	@echo '	make <target>'
	@echo ''
	@echo 'Targets:'
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


all: ## run all
	src

src: ## deploy doc
	@$(SPHINXBUILD) -M $(TOHTML) "$(SOURCEDIR)$(SRC)" "$(BUILDDIR)$(SRC)" $(SPHINXOPTS) $(O)

watch-deployment: ## deploy in watch mode
	find .$(DEPLOYMENT)/*.rst | entr make src
