README for wcc.prayercycle
==========================================

Prayer Cycle content type for Plone that provides a Prayer Cycle event type,
and portlets to show upcoming, and current prayers for the month.

Usage
=====

 * Install Prayer Cycle as a Plone product.
 * Add Prayer Cycles (probably in a folder).
 * Assign upcoming and current prayer cycle portlets
   to pages you would like them to be displayed.

Embedding
---------

For Blogger and websites compatible with Web Gadgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Web Gadget is an easy way to plug dynamic content into a blog. In Blogger,
all you need to do is to configure the layout of your page, click "Add Gadget"
and select "Add your own". The dialogue box asks you for a URL.

The URL for the Prayer Cycle Gadget is: 
http://yoursitehostanem/currentprayercycle.xml

For other websites
~~~~~~~~~~~~~~~~~~

If you can edit the HTML template or be able to embed HTML on your
website ::

	<div style="border:solid 1px #ddd; width:150px; background-color:#fff;">
	<h4 style="text-align:center;">This week we pray for</h4>
	<iframe src="http://yoursitename/currentprayercycle.html" allowTransparency="true" width="150" height="235" scrolling="no" frameborder="0">Your browser doesn't display Frames</iframe>
	</div>


Customize the look of the prayer cycle item

You may also use your own CSS style sheet to customize the look of the prayer
cycle item. On the given code, replace

http://yoursitehostname/currentprayercycle.html
with:

http://yoursitehostname/currentprayercycle.html?css=http://www.mysite.org/mystyles.css
where http://www.mysite.org/mystyles.css is the url to your style sheet.


Include the prayer cycle on the server side with PHP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The prayer cycle can also be included so that it becomes part of a page. In
PHP, the following piece of code will do the job ::

	<?php
	$handle = fopen("http://www.oikoumene.org/en/currentprayercycle.html?format=raw", "rb");
	$contents = stream_get_contents($handle);
	fclose($handle);
	echo $contents;
	?>
Please note that this will provide you raw unstyled content.


