/*
  Warnings:

  - You are about to drop the `FactionRanks` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `FactionRanks` DROP FOREIGN KEY `FactionRanks_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitAlleigance` DROP FOREIGN KEY `UnitAlleigance_faction_rank_id_fkey`;

-- DropTable
DROP TABLE `FactionRanks`;

-- CreateTable
CREATE TABLE `FactionRank` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NULL,
    `rank` INTEGER NOT NULL DEFAULT 1,
    `faction_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `FactionRank` ADD CONSTRAINT `FactionRank_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitAlleigance` ADD CONSTRAINT `UnitAlleigance_faction_rank_id_fkey` FOREIGN KEY (`faction_rank_id`) REFERENCES `FactionRank`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
