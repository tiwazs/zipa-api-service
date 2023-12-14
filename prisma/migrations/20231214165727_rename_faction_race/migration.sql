/*
  Warnings:

  - You are about to drop the column `faction_id` on the `Unit` table. All the data in the column will be lost.
  - You are about to drop the `Faction` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `FactionTrait` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `FactionUnitSpecialization` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `race_id` to the `Unit` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE `FactionTrait` DROP FOREIGN KEY `FactionTrait_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionTrait` DROP FOREIGN KEY `FactionTrait_trait_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionUnitSpecialization` DROP FOREIGN KEY `FactionUnitSpecialization_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionUnitSpecialization` DROP FOREIGN KEY `FactionUnitSpecialization_unit_specialization_id_fkey`;

-- DropForeignKey
ALTER TABLE `Unit` DROP FOREIGN KEY `Unit_faction_id_fkey`;

-- AlterTable
ALTER TABLE `Unit` DROP COLUMN `faction_id`,
    ADD COLUMN `race_id` VARCHAR(191) NOT NULL;

-- DropTable
DROP TABLE `Faction`;

-- DropTable
DROP TABLE `FactionTrait`;

-- DropTable
DROP TABLE `FactionUnitSpecialization`;

-- CreateTable
CREATE TABLE `Race` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NOT NULL,
    `identity` TEXT NULL,
    `aspects` TEXT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `RaceTrait` (
    `id` VARCHAR(191) NOT NULL,
    `race_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `conditions` VARCHAR(191) NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `RaceTrait` ADD CONSTRAINT `RaceTrait_race_id_fkey` FOREIGN KEY (`race_id`) REFERENCES `Race`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RaceTrait` ADD CONSTRAINT `RaceTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Unit` ADD CONSTRAINT `Unit_race_id_fkey` FOREIGN KEY (`race_id`) REFERENCES `Race`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
