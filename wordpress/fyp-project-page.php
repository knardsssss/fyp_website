<?php
/**
 * Plugin Name: FYP Project Page
 * Description: Displays the investment-assistant project record using [fyp_project_page].
 * Version: 1.0.0
 */
if (!defined('ABSPATH')) { exit; }

function fyp_project_page_styles() {
    // Load on the public site so shortcodes in page builders/templates also receive styles.
    wp_enqueue_style('fyp-project-page', plugins_url('styles.css', __FILE__), array(), filemtime(__DIR__ . '/styles.css'));
}
add_action('wp_enqueue_scripts', 'fyp_project_page_styles');

function fyp_project_page_render() {
    // This is a bundled static template; no request data is interpolated.
    return file_get_contents(__DIR__ . '/content.html');
}
add_shortcode('fyp_project_page', 'fyp_project_page_render');
