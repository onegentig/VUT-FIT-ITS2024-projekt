ZIP_NAME=xonege00.zip

phony: zip test full-test doc format ocstart ocstop oclogs ocrm

########## Zipping, docs etc. ##########

zip: $(ZIP_NAME)

doc: report.pdf

$(ZIP_NAME): report.pdf
	zip -9 -v $(ZIP_NAME) report.pdf requirements.txt features/environment.py features/*.feature features/steps/*.py

report.pdf: docs/report.typ
	typst compile docs/report.typ
	mv docs/report.pdf .

format:
	black features/*.py features/steps/*.py

########## OpenCart & Selenium ##########

test:
	behave

full-test: ocstart
	[ -f "requirements.txt" ] && pip3 install -r requirements.txt
	behave || true
	docker-compose down -v

ocstart: docker-compose.yml
	docker-compose up -d
	@sleep 3

ocstop:
	docker-compose down

oclogs:
	docker-compose logs -f

ocrm:
	docker-compose rm -f
