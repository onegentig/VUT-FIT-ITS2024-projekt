ZIP_NAME=xkrame00.zip

phony: zip test full doc format ocstart ocstop oclogs ocrm

########## Zipping, docs etc. ##########

zip: $(ZIP_NAME)

doc: report.pdf

$(ZIP_NAME): report.pdf
	zip -9 -v $(ZIP_NAME) report.pdf requirements.txt features/environment.py features/*.feature features/steps/*.py

report.pdf: docs/report.typ
	typst compile docs/report.typ
	mv docs/report.pdf .

format:
	black features/*.py features/steps/*.py features/lib/*.py

########## OpenCart & Selenium ##########

test:
	behave

full: ocstart
	[ -f "requirements.txt" ] && pip3 install -r requirements.txt
	behave || true
	docker-compose down -v

ocstart: docker-compose.yml
	docker-compose up -d

ocstop:
	docker-compose down

oclogs:
	docker-compose logs -f

ocrm:
	docker-compose rm -f
