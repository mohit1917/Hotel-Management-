-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2022 at 06:58 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel management`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `fullname` varchar(1000) NOT NULL,
  `contactno` varchar(1000) NOT NULL,
  `emailid` varchar(1000) NOT NULL,
  `gender` varchar(1000) NOT NULL,
  `checkin` varchar(1000) NOT NULL,
  `checkout` varchar(1000) NOT NULL,
  `rooms` varchar(100) NOT NULL,
  `guests` varchar(100) NOT NULL,
  `smookingroom` varchar(100) NOT NULL,
  `largebed` varchar(100) NOT NULL,
  `earlylcheckin` varchar(100) NOT NULL,
  `latecheckin` varchar(100) NOT NULL,
  `roomonahighfloor` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `fullname`, `contactno`, `emailid`, `gender`, `checkin`, `checkout`, `rooms`, `guests`, `smookingroom`, `largebed`, `earlylcheckin`, `latecheckin`, `roomonahighfloor`) VALUES
(1, 'NancyNohria', '6284023415', 'softwizznancy@gmail.com`', 'Female', '26/05', '28/05', '1', '2', '0', '0', '1', '1', '1'),
(2, 'Mohit', '6284023415', 'mg281809@gmail.com', 'Male', '26/05', '28/05', '1', '2', '0', '1', '0', '1', '1'),
(3, 'Mahii', '6284023415', 'mahi213@gmail.com', 'Male', '26/05', '28/05', '2', '4', '0', '0', '1', '1', '1'),
(4, 'Arushi', '788574596', 'arushui@gmail.com', 'Female', '28/01', '30/01', '3', '6', '0', '0', '1', '1', '1'),
(5, 'Tarisha', '6523652325', 'tarisha@gmail.com', 'Female', '25/01', '28/01', '2', '4', '0', '0', '1', '1', '1'),
(6, 'kashish', '6284026415', 'kashish@gmail.com', 'Female', '21/05', '24/05', '2', '4', '0', '1', '1', '1', '0'),
(7, 'Vivek', '6284356429', 'vivek0359@gmail.com', 'Male', '28/02', '29/02', '3', '6', '1', '1', '0', '0', '1'),
(8, 'Harman', '6284023415', 'harman@gmail.com', 'Male', '25/02', '28/02', '1', '2', '0', '0', '0', '1', '1'),
(9, 'Sharu', '6245468566', 'sharu@gmail.com', 'Male', '28/02', '29/02', '2', '4', '1', '1', '0', '1', '0'),
(10, 'Navjot', '6258965896', 'navjot@gmail.com', 'Female', '25/05', '28/05', '3', '6', '0', '0', '1', '1', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
