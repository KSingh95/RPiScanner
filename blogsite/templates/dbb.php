<?php
// Connecting, selecting database

$conn = pg_connect("host=localhost dbname=rpidata user=postgres password=1995")
    or die('Could not connect: ' . pg_last_error());
