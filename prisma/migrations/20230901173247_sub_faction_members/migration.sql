/*
  Warnings:

  - You are about to drop the `UnitAlleigance` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `UnitAlleigance` DROP FOREIGN KEY `UnitAlleigance_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitAlleigance` DROP FOREIGN KEY `UnitAlleigance_faction_rank_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitAlleigance` DROP FOREIGN KEY `UnitAlleigance_unit_id_fkey`;

-- DropTable
DROP TABLE `UnitAlleigance`;

-- CreateTable
CREATE TABLE `SubFactionMember` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `faction_rank_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `SubFactionMember` ADD CONSTRAINT `SubFactionMember_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SubFactionMember` ADD CONSTRAINT `SubFactionMember_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SubFactionMember` ADD CONSTRAINT `SubFactionMember_faction_rank_id_fkey` FOREIGN KEY (`faction_rank_id`) REFERENCES `FactionRank`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
