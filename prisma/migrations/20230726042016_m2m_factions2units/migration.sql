/*
  Warnings:

  - You are about to drop the column `faction_id` on the `Unit` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE `Unit` DROP FOREIGN KEY `Unit_faction_id_fkey`;

-- AlterTable
ALTER TABLE `Unit` DROP COLUMN `faction_id`;

-- CreateTable
CREATE TABLE `FactionUnit` (
    `id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `FactionUnit` ADD CONSTRAINT `FactionUnit_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionUnit` ADD CONSTRAINT `FactionUnit_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
