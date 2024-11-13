<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'rl_4' );

/** Database username */
define( 'DB_USER', 'andysurprj2_db' );

/** Database password */
define( 'DB_PASSWORD', '3vLDpQ@8jWksFPz^nGcxZ7Bq6Rtm!U4JH0AweSYb*9N1fh!dV5Erjl2X#0KyQo&T' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'KJHJK756HGJJG^%$^565&^FHG%^$C54%$$GC45%$$%)_()*23CGH' );
define( 'SECURE_AUTH_KEY',  'JKHBHJ%^%$(*&@#$7984HJD5476(*#$lknDR(NU@RC&NVHGVHG76' );
define( 'LOGGED_IN_KEY',    'LSDJKN*^$H$OFU(#(#@BJAK PQWMFVF%#_(HADP3746IONF*WVDO' );
define( 'NONCE_KEY',        'JKHBHJ%^%$(*&@#$7984HJD5476(*#$lknDR(NU@RC&NVHGVHG76' );
define( 'AUTH_SALT',        'KJBH&^%&^GHJG$#$#$GJKJOSD(*(OSJD#(RJGUBVO857JFBSKIEY' );
define( 'SECURE_AUTH_SALT', 'LSKDJKB@%)!#NF^!)#RNGFNV__#Y$BQYYBD@#^##BBBBD@@&T$NU' );
define( 'LOGGED_IN_SALT',   'LKSJKDS(&$#KNDN^&@Y@J@***NCJ@GUB)ND@UB@EKEY(@RDBHSBC' );
define( 'NONCE_SALT',       'MALZBVOQYFPNQPPQBXL&#&%^86363B^y3r67ubx76%@*B83nrJBS' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'rldb_4_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
