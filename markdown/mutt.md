# mutt send mail

## 1. add file .muttrc

	set sendmail="/usr/bin/msmtp"
	set use_from=yes
	set realname="name"
	set from="tengfei.wang@goocan.net"
	set envelope_from=yes

## 2. add file .msmtprc

##### Accounts will inherit settings from this section
	defaults
##### A first gmail address
	account        gmail
	host           smtp.gmail.com
	port           587
	from           username@gmail.com
	user           username@gmail.com
	password       password
	tls_trust_file /etc/ssl/certs/ca-certificates.crt
##### A second gmail address
	account    gmail2 : gmail
	from       username2@gmail.com
	user       username2@gmail.com
	password   password2
##### A freemail service
	account    freemail
	host       smtp.freemail.example
	from       joe_smith@freemail.example
	user       joe.smith
	password   secret
##### A provider's service
	account   provider
	host      smtp.provider.example
##### A emali
	account    gucan
	host       smtp.exmail.qq.com
	port       25
	from       tengfei.wang@goocan.net
	auth       login
	tls        off
	user       tellngfei.wang@goocan.net
	password   tengfei2008
	logfile    ~/.msmtp.log
##### Set a default account
	account default : gucan

## 3. send mail
	mutt 750800292@qq.com -s 'x' -m 'm'