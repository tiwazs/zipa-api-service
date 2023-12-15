/*
  Warnings:

  - You are about to drop the `SubFaction` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `SubFactionMember` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `FactionRank` DROP FOREIGN KEY `FactionRank_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionRelation` DROP FOREIGN KEY `FactionRelation_faction2_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionRelation` DROP FOREIGN KEY `FactionRelation_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `SubFaction` DROP FOREIGN KEY `SubFaction_user_id_fkey`;

-- DropForeignKey
ALTER TABLE `SubFactionMember` DROP FOREIGN KEY `SubFactionMember_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `SubFactionMember` DROP FOREIGN KEY `SubFactionMember_faction_rank_id_fkey`;

-- DropForeignKey
ALTER TABLE `SubFactionMember` DROP FOREIGN KEY `SubFactionMember_unit_id_fkey`;

-- DropTable
DROP TABLE `SubFaction`;

-- DropTable
DROP TABLE `SubFactionMember`;

-- CreateTable
CREATE TABLE `Faction` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NULL,
    `holdings` VARCHAR(191) NULL,
    `user_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `FactionMember` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `faction_rank_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Faction` ADD CONSTRAINT `Faction_user_id_fkey` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRank` ADD CONSTRAINT `FactionRank_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionMember` ADD CONSTRAINT `FactionMember_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionMember` ADD CONSTRAINT `FactionMember_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionMember` ADD CONSTRAINT `FactionMember_faction_rank_id_fkey` FOREIGN KEY (`faction_rank_id`) REFERENCES `FactionRank`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRelation` ADD CONSTRAINT `FactionRelation_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRelation` ADD CONSTRAINT `FactionRelation_faction2_id_fkey` FOREIGN KEY (`faction2_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
