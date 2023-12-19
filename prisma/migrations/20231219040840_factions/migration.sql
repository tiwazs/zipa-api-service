/*
  Warnings:

  - Added the required column `belief_id` to the `Faction` table without a default value. This is not possible if the table is not empty.
  - Added the required column `culture_id` to the `Faction` table without a default value. This is not possible if the table is not empty.
  - Added the required column `race_id` to the `Faction` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `Faction` ADD COLUMN `belief_id` VARCHAR(191) NOT NULL,
    ADD COLUMN `culture_id` VARCHAR(191) NOT NULL,
    ADD COLUMN `race_id` VARCHAR(191) NOT NULL;

-- AddForeignKey
ALTER TABLE `Faction` ADD CONSTRAINT `Faction_race_id_fkey` FOREIGN KEY (`race_id`) REFERENCES `Race`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Faction` ADD CONSTRAINT `Faction_culture_id_fkey` FOREIGN KEY (`culture_id`) REFERENCES `Culture`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Faction` ADD CONSTRAINT `Faction_belief_id_fkey` FOREIGN KEY (`belief_id`) REFERENCES `Belief`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
