/*
  Warnings:

  - Added the required column `belief_id` to the `Unit` table without a default value. This is not possible if the table is not empty.
  - Added the required column `culture_id` to the `Unit` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `Unit` ADD COLUMN `belief_id` VARCHAR(191) NOT NULL,
    ADD COLUMN `culture_id` VARCHAR(191) NOT NULL;

-- AddForeignKey
ALTER TABLE `Unit` ADD CONSTRAINT `Unit_culture_id_fkey` FOREIGN KEY (`culture_id`) REFERENCES `Culture`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Unit` ADD CONSTRAINT `Unit_belief_id_fkey` FOREIGN KEY (`belief_id`) REFERENCES `Belief`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
