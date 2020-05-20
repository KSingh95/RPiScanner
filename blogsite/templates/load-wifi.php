<?php
    include dbb.php

        $query = 'SELECT * FROM wifi';
        $result = pg_query($query) or die('Query failed: ' . pg_last_error());
        while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
            echo "<p>";
            foreach ($line as $col_value) {
                echo "\t\t<td>$col_value</td>\n";
            }
        }
?>