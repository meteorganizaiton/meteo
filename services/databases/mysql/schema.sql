CREATE DATABASE meteo_db;

use meteo_db;

CREATE TABLE `locations` (
  `id` integer PRIMARY KEY,
  `city_name` varchar(255),
  `country_code` varchar(255),
  `timezone` integer,
  `coord` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `location_weather` (
  `id` integer PRIMARY KEY,
  `display_name` varchar(255),
  `description` varchar(255),
  `display_icon` varchar(255),
  `extra_data` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp
);

ALTER TABLE `locations` ADD FOREIGN KEY (`id`) REFERENCES `location_weather` (`id`);
