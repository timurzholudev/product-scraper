<h1># product-scraper</h1>
Scraper which get your list of products (on Amazon) and and price you want, then send you email when price drops

<h2>App setup</h2>
<p>First setup yout gmail to send email from app:</p>
<ul>
	<li>Allow Less secure app access</li>
	<li>Set 2-Step Verification</li>
	<li>Set google App passwords, in dropdown options choose next:
		<ul>
			<li>Select app - <b>Mail</b></li>
			<li>Select device - <b>Windows</b></li>
		</ul>
	</li>
</ul>

<p>Then update next fields in scraper.py:</p>
<b>smtp_link 				= 'smtp.gmail.com'</b>
<br/><b>smtp_port 	= 587</b>
<br/><b>auth_email 	= 'email_from_send@example.com'</b>
<br/><b>auth_pass 	= 'email_app_pass'</b>
<br/><b>email_to 		= 'email_to_send@example.com'</b>
<br/><b>sleep_time 	= 60</b>
