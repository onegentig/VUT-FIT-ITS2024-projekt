ZIP_NAME=xkrame00.zip

###############################################################################

phony: zip ocstart ocstop oclogs ocrm

########## Zipping and docs ##########

zip: $(ZIP_NAME)

$(ZIP_NAME):
	zip -9 -v $(ZIP_NAME) README.md *.feature

README.pdf: README.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o $@

########## OpenCart ##########

docker-compose.yml:
	curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/opencart/docker-compose.yml > docker-compose.yml

ocstart: docker-compose.yml
	docker-compose up -d
	@sleep 3

ocstop:
	docker-compose down

oclogs:
	docker-compose logs -f

ocrm:
	docker-compose rm -f
